import json
import subprocess
from typing import List


def ansible_modules() -> List[str]:
    """Returns list of install ansible modules"""
    print("Gathering list of installed ansible modules...")
    result = []

    data = json.loads(
        subprocess.check_output(["ansible-doc", "-j", "-l"], universal_newlines=True)
    )
    for module in data.keys():
        result.append(module)

    return result
