"""Rebuilds JSON Schemas from our models."""
import copy
import glob
import json
import multiprocessing
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, List

import requests
from rich.progress import Progress

from ansibleschemas._modules import ANSIBLE_MODULES
from ansibleschemas.ansiblelint import AnsibleLintModel
from ansibleschemas.galaxy import GalaxyFileModel
from ansibleschemas.meta import MetaModel
from ansibleschemas.molecule import MoleculeScenarioModel
from ansibleschemas.playbook import PlaybookFileModel
from ansibleschemas.requirements import RequirementsFileModel
from ansibleschemas.tasks import TaskModel
from ansibleschemas.vars import VarsModel

# Not really Ansible schemas, but included for convenience
from ansibleschemas.zuul import ZuulConfigModel

GALAXY_API_URL = "https://galaxy.ansible.com"
out_dir = Path(os.getcwd()) / "f"
module_dir = Path(__file__).resolve().parents[0]
GENERATED_HEADER = "# pylint: disable-all\n"


def dump_galaxy_platforms() -> None:
    """Dumps galaxy platforms into a python module."""
    filename = f"{module_dir}/_galaxy.py"
    print(f"Dumping list of Galaxy platforms to {filename}")
    platforms: Dict[str, List[str]] = {}
    result = {'next_link': '/api/v1/platforms/'}
    while result.get('next_link', None):
        url = GALAXY_API_URL + result['next_link']
        result = requests.get(url).json()
        for entry in result['results']:
            if not isinstance(entry, dict):
                continue
            name = entry.get('name', None)
            release = entry.get('release', None)
            if not name or not isinstance(name, str):
                continue
            if name and name not in platforms:
                platforms[name] = []
            if release not in ['any', 'None'] and release not in platforms[name]:
                platforms[name].append(release)

    with open(filename, "w") as file:
        file.write(GENERATED_HEADER + f"\nGALAXY_PLATFORMS = {platforms}\n")


def dump_ansible_modules() -> None:
    """Dumps ansible module list into a python module."""
    print("Dumping list of Ansible modules")
    #  ansible-doc command dumps modules in unpredictable order
    result = subprocess.run(
        "ansible-doc -j -l",
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,  # dump garbage warnings
    )
    modules = sorted(json.loads(result.stdout).keys())
    with open(f"{module_dir}/_modules.py", "w") as file:
        file.write(GENERATED_HEADER + f"\nANSIBLE_MODULES = {modules}\n")


def dump_module_doc(module):
    """Dumps module docs as json."""
    os.system(f"ansible-doc -j {module} > data/modules/{module}.json")
    return module


def doc_dump() -> None:
    """Dump documentation for all Ansible modules."""
    with Progress() as progress:
        results = []
        task_id = progress.add_task("Dumping doc for each module ...", total=len(ANSIBLE_MODULES))
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            for result in pool.imap(dump_module_doc, ANSIBLE_MODULES):
                results.append(result)
                progress.advance(task_id)


def map_type(ansible_type: str) -> str:
    """Return JSON date type for a given Ansible type."""
    # https://json-schema.org/understanding-json-schema/reference/type.html
    # raw is used for file mode by ansible
    if ansible_type in ['str', 'filename', 'path', 'raw', 'sid']:
        return 'string'
    if ansible_type == 'list':
        return 'array'
    if ansible_type == 'bool':
        return 'boolean'
    if ansible_type == 'int':
        return 'integer'
    if ansible_type in ['dict', 'jsonarg', 'json']:
        return 'object'
    if ansible_type == 'float':
        return 'number'
    raise NotImplementedError(f"Unable to map ansible type {ansible_type} to JSON Schema type.")


def export_module_schemas() -> None:
    # Alternative approach of combining all modules into a single BeremothModel,
    # which seems to produce ~1.1mb file.
    # kwargs = dict()
    definitions: Dict[str, Any] = {}
    items: List[Dict[str, str]] = []
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema",
        "definitions": definitions,
        "title": "Ansible Tasks Schema",
        "type": "array",
        "examples": [
            "tasks/*.yml",
            "handlers/*.yml"
        ],
        "items": {
            "anyOf": items
        }
    }
    with open("data/ansible-base-task.json") as json_file:
        json_string = json_file.read()
        base_task_definition = json.loads(json_string)

    for filename in sorted(glob.glob("data/modules/*.json")):
        module = os.path.splitext(os.path.basename(filename))[0]
        # if "." in module:
        #     continue

        definition = copy.deepcopy(base_task_definition)
        properties: Dict[str, Dict[str, str]] = {}
        required: List[str] = []
        args = {
            "type": "object",
            "properties": properties,
            "required": required,
            "additionalProperties": False}
        definition['properties'][module] = args
        if "required" not in definition:
            definition["required"] = []
        definition["required"].append(module)
        items.append({"$ref": f"#/definitions/{module}"})
        with open(filename) as json_file:
            print(filename)
            json_string = json_file.read()
            if not json_string:
                print(f"WARNING: Skipping module without doc: {filename}")
                continue
            try:
                data = json.loads(json_string)[module]
                title = data['doc']['short_description']
                description = "\n".join(data['doc']['description'])
                for property, value in data['doc'].get("options", {}).items():
                    # description can be list of strings
                    o_desc = value['description']
                    if not isinstance(o_desc, str):
                        o_desc = "\n".join(o_desc)
                    args['title'] = o_desc
                    properties[property] = {}
                    if 'type' in value:
                        properties[property]['type'] = map_type(value['type'])
                    if value.get("required", False):
                        required.append(property)

            except Exception as ex:
                raise RuntimeError(f"Failed to load {filename}: %s" % ex)

        definition['title'] = title
        definition['description'] = description
        definitions[module] = definition

    with open("f/ansible-tasks.json", "w") as f:
        f.write(json.dumps(schema, indent=2, sort_keys=True))


def main() -> None:
    """Main entry point"""

    dump_galaxy_platforms()
    dump_ansible_modules()

    schemas = {
        "ansible-lint": AnsibleLintModel,
        "galaxy": GalaxyFileModel,
        "meta": MetaModel,
        "molecule": MoleculeScenarioModel,
        "playbook": PlaybookFileModel,
        "requirements": RequirementsFileModel,
        # "tasks": TasksListModel,
        "vars": VarsModel,
        "zuul": ZuulConfigModel,
        "base-task": TaskModel
    }
    schema_filenames = {
        "ansible-lint": "ansible-lint",
        "galaxy": "ansible-galaxy",
        "meta": "ansible-meta",
        "molecule": "molecule",
        "playbook": "ansible-playbook",
        "requirements": "ansible-requirements",
        # "tasks": "ansible-tasks",
        "base-task": "../data/ansible-base-task",
        "vars": "ansible-vars",
        "zuul": "zuul",
    }

    for schema, model in schemas.items():
        print(f"Building schema for {schema}")

        output_file = out_dir / f"{schema_filenames[schema]}.json"
        with open(output_file, "w") as file:
            file.write(model.schema_json(
                indent=2,
                sort_keys=True))
            # by_alias
            # skip_defaults
            # exclude_unset
            # exclude_defaults
            # exclude_none
            # include
            # exclude
            # encoder function, defaults to json.dumps()
            file.write("\n")

    export_module_schemas()


if __name__ == "__main__":
    main()
