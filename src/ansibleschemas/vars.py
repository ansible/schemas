# Used to generate JSON Validations Schema for requirements.
import re
from typing import Any, Mapping, Union

from pydantic import BaseModel, ConstrainedStr

from . import consts


class EncryptedString(ConstrainedStr):
    regex = re.compile(r'^\$ANSIBLE_VAULT;')


class VarsModel(BaseModel):
    __root__: Union[Mapping[str, Any], EncryptedString]

    class Config:
        title = "Ansible Vars Schema"

        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
            "examples": [
                "playbooks/vars/*.yml",
                "vars/*.yml",
                "defaults/*.yml",
                "host_vars/*.yml",
                "group_vars/*.yml",
            ],
        }
