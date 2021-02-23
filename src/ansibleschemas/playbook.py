# Used to generate JSON Validations chema for requirements.
import sys
from typing import Any, List, Mapping, Optional, Union

from pydantic import BaseModel, Extra

from ansibleschemas.tasks import TaskModel, _SharedModel

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


class PlayModel(_SharedModel):
    # based on https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#play
    fact_path: Optional[str]
    force_handlers: Optional[bool]
    gather_facts: Optional[bool]
    gather_subset: Optional[bool]
    gather_timeout: Optional[int]
    handlers: Optional[List[TaskModel]]
    hosts: str  # REQUIRED
    max_fail_percentage: Optional[float]
    order: Optional[
        Literal["default", "sorted", "reverse_sorted", "reverse_inventory", "shuffle"]
    ]
    post_tasks: Optional[List[TaskModel]]
    pre_tasks: Optional[List[TaskModel]]
    roles: Optional[List[Union[RoleModel, str]]]
    serial: Optional[int]
    strategy: Optional[str]
    tasks: Optional[List[TaskModel]]
    vars_files: Optional[List[str]]
    vars_prompt: Optional[List[str]]

    class Config:
        extra = Extra.forbid


class ImportPlaybookModel(BaseModel):
    import_playbook: str

    class Config:
        extra = Extra.forbid


class PlaybookFileModel(BaseModel):
    __root__: List[Union[PlayModel, ImportPlaybookModel]]

    class Config:
        extra = Extra.forbid
        title = "Ansible Playbook Schema"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
        }
