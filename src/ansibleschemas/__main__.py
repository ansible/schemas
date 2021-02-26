"""Rebuilds JSON Schemas from our models."""
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List

import requests

from ansibleschemas.meta import MetaModel
from ansibleschemas.playbook import PlaybookFileModel
from ansibleschemas.requirements import RequirementsFileModel
from ansibleschemas.tasks import TasksFileModel
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


def main() -> None:
    """Main entry point"""
    dump_galaxy_platforms()
    dump_ansible_modules()

    schemas = {
        "meta": MetaModel,
        "playbook": PlaybookFileModel,
        "requirements": RequirementsFileModel,
        "tasks": TasksFileModel,
        "vars": VarsModel,
        "zuul": ZuulConfigModel,
    }
    schema_filenames = {
        "meta": "ansible-meta",
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


if __name__ == "__main__":
    main()
