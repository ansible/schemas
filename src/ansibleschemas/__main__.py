"""Rebuilds JSON Schemas from our models."""
import glob
import json
import multiprocessing
import os
import subprocess
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from pathlib import Path

import requests
from rich.progress import Progress

from ansibleschemas._galaxy import GALAXY_PLATFORMS
from ansibleschemas.ansiblelint import AnsibleLintModel
from ansibleschemas.api import ansible_modules
from ansibleschemas.galaxy import GalaxyFileModel
from ansibleschemas.meta import MetaModel
from ansibleschemas.molecule import MoleculeModel
from ansibleschemas.playbook import PlaybookFileModel
from ansibleschemas.requirements import RequirementsFileModel
from ansibleschemas.tasks import TasksListModel
from ansibleschemas.vars import VarsModel

# Not really Ansible schemas, but included for convenience
from ansibleschemas.zuul import ZuulConfigModel

GALAXY_API_URL = "https://galaxy.ansible.com"
out_dir = Path(os.getcwd()) / "f"
module_dir = Path(__file__).resolve().parents[0]

GALAXY_FILE_HEADER = """from typing import Dict, List

GALAXY_PLATFORMS: Dict[str, List[str]]"""


def parse_args() -> Namespace:
    """Parse commandline arguments."""

    example_text = """
examples:
  generate schemas without fetching any external data:
    ansibleschemas

  update the list of Galaxy platforms and generate schemas:
    ansibleschemas --dump-galaxy-platforms
"""

    parser = ArgumentParser(
        description="Generate JSON/YAML Validation schemas for Ansible content.",
        prog="ansibleschemas",
        epilog=example_text,
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        '-p',
        '--dump-galaxy-platforms',
        default=os.environ.get('DUMP_GALAXY_PLATFORMS'),
        action='store_true',
        help="Query the Galaxy API and dump all Galaxy platforms into a python module.",
    )
    return parser.parse_args()


def pretty_plattforms(value: dict) -> str:
    """Pretty prints the plattform dictionary"""
    items = [
        '\n' + ' ' * 4 + repr(key) + ': ' + _pretty_list(value[key], len(repr(key)))
        for key in value
    ]
    return '{%s}' % (','.join(items) + ',\n')


def _pretty_list(value: list, key_length: int) -> str:
    """Pretty prints a list. Automatically warps lines if line length of 88 is exceeded (-> black compatibility)."""
    htchar = ' '
    indent = 4
    nlch = '\n' + htchar * indent
    items = [repr(item) for item in value]
    if (len(', '.join(items)) + key_length + 9) > 88:
        return '[%s]' % (
            nlch
            + htchar * indent
            + (',' + nlch + htchar * indent).join(items)
            + ','
            + nlch
        )
    return '[%s]' % (', '.join(items))


def dump_galaxy_platforms() -> None:
    """Dumps galaxy platforms into a python module."""
    filename = f"{module_dir}/_galaxy.py"
    print(f"Dumping list of Galaxy platforms to {filename}")
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
            if name and name not in GALAXY_PLATFORMS:
                GALAXY_PLATFORMS[name] = []
            if (
                release not in ['any', 'all', 'None']
                and release not in GALAXY_PLATFORMS[name]
            ):
                GALAXY_PLATFORMS[name].append(release)
                GALAXY_PLATFORMS[name].sort()

    with open(filename, "w") as file:
        file.write(f"{GALAXY_FILE_HEADER} = {pretty_plattforms(GALAXY_PLATFORMS)}\n")


def dump_module_doc(module):
    """Dumps module docs as json."""
    try:
        module_json = subprocess.check_output(
            ["ansible-doc", "-j", module], universal_newlines=True
        )
        data = json.loads(module_json)
        # we remove filename from the dump as that prevents reproduceble builds as
        # they are full paths.
        data[module]["doc"].pop("filename", None)
        # removed as not being used by us (performance)
        data[module]["doc"].pop("author", None)
        data[module]["doc"].pop("notes", None)
        data[module]["doc"].pop("examples", None)
        data[module]["doc"].pop("return", None)

        with open(f"data/modules/{module}.json", "w") as file:
            file.write(json.dumps(data, indent=2, sort_keys=True))
            file.write("\n")
    except subprocess.CalledProcessError:
        print(f"Module {module} skipped as it failed to export documentation.")
    return module


def doc_dump() -> None:
    """Dump documentation for all Ansible modules."""
    files = glob.glob('data/modules/*.json')
    for file in files:
        os.remove(file)

    modules = list(ansible_modules())
    with Progress() as progress:
        results = []
        task_id = progress.add_task(
            "Dumping doc for each module ...", total=len(modules)
        )
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            for result in pool.imap(dump_module_doc, modules):
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
    raise NotImplementedError(
        f"Unable to map ansible type {ansible_type} to JSON Schema type."
    )


def main() -> None:
    """Main entry point"""

    args = parse_args()

    if args.dump_galaxy_platforms:
        dump_galaxy_platforms()

    schemas = {
        "ansible-lint": AnsibleLintModel,
        "galaxy": GalaxyFileModel,
        "meta": MetaModel,
        "molecule": MoleculeModel,
        "playbook": PlaybookFileModel,
        "requirements": RequirementsFileModel,
        "tasks": TasksListModel,
        "vars": VarsModel,
        "zuul": ZuulConfigModel,
    }
    schema_filenames = {
        "ansible-lint": "ansible-lint",
        "galaxy": "ansible-galaxy",
        "meta": "ansible-meta",
        "molecule": "molecule",
        "playbook": "ansible-playbook",
        "requirements": "ansible-requirements",
        "tasks": "ansible-tasks",
        "vars": "ansible-vars",
        "zuul": "zuul",
    }

    for schema, model in schemas.items():
        print(f"Building schema for {schema}")

        output_file = out_dir / f"{schema_filenames[schema]}.json"
        with open(output_file, "w") as file:
            file.write(model.schema_json(indent=2, sort_keys=True))
            # by_alias
            # skip_defaults
            # exclude_unset
            # exclude_defaults
            # exclude_none
            # include
            # exclude
            # encoder function, defaults to json.dumps()
            file.write("\n")


if __name__ == "__main__":
    main()
