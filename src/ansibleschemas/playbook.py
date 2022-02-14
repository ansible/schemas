# Used to generate JSON Validations Schema for playbooks.
import sys
from typing import Any, List, Mapping, Optional, Union

from pydantic import BaseModel, Extra

from ansibleschemas.tasks import TasksListModel, _SharedModel

from . import consts

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal


class RoleModel(_SharedModel):
    role: str
    delegate_to: Optional[str]
    vars: Optional[Mapping[str, Any]]
    tags: Optional[List[str]]


class VarsPromptModel(BaseModel):
    # https://docs.ansible.com/ansible/latest/user_guide/playbooks_prompts.html
    name: str
    prompt: str
    private: Optional[bool] = True
    encrypt: Optional[
        Literal[
            "des_crypt",
            "bsdi_crypt",
            "bigcrypt",
            "crypt16",
            "md5_crypt",
            "bcrypt",
            "sha1_crypt",
            "sun_md5_crypt",
            "sha256_crypt",
            "sha512_crypt",
            "apr_md5_crypt",
            "phpass",
            "pbkdf2_digest",
            "cta_pbkdf2_sha1",
            "dlitz_pbkdf2_sha1",
            "scram",
            "bsd_nthash",
        ]
    ]
    confirm: Optional[bool]
    salt_size: Optional[int] = 8


class PlayModel(_SharedModel):
    # based on https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#play
    fact_path: Optional[str]
    force_handlers: Optional[bool]
    gather_facts: Optional[bool]
    gather_subset: Optional[bool]
    gather_timeout: Optional[int]
    handlers: Optional[TasksListModel]
    hosts: Union[str, List[str]]  # REQUIRED
    max_fail_percentage: Optional[float]
    order: Optional[
        Literal["default", "sorted", "reverse_sorted", "reverse_inventory", "shuffle"]
    ]
    post_tasks: Optional[TasksListModel]
    pre_tasks: Optional[TasksListModel]
    roles: Optional[List[Union[RoleModel, str]]]
    serial: Optional[Union[int, str, List[Union[int, str]]]]
    strategy: Optional[str]
    tasks: Optional[TasksListModel]
    vars_files: Optional[List[str]]
    vars_prompt: Optional[List[VarsPromptModel]]

    class Config:
        extra = Extra.forbid


class ImportPlaybookModel(BaseModel):
    name: Optional[str]
    import_playbook: str
    vars: Optional[Mapping[str, Any]]

    class Config:
        extra = Extra.forbid


class PlaybookFileModel(BaseModel):
    __root__: List[Union[ImportPlaybookModel, PlayModel]]

    class Config:
        extra = Extra.forbid
        title = "Ansible Playbook Schema"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
            "examples": ["playbooks/*.yml", "playbooks/*.yaml"],
        }
