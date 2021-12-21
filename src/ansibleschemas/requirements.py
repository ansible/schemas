# Used to generate JSON Validations Schema for requirements.
import sys
from typing import List, Optional, Union

from pydantic import BaseModel, Extra

from . import consts

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal


class CollectionModel(BaseModel):
    # https://docs.ansible.com/ansible/latest/galaxy/user_guide.html
    name: Optional[str]
    version: Optional[str]
    type: Optional[Literal["galaxy", "url", "file", "git"]]
    # We do not use HttpUrl because it produces schema with format: uri, which
    # seems to fail ajv validation with:
    # unknown format "uri" ignored in schema at path
    source: Optional[str]

    class Config:
        extra = Extra.forbid


class CollectionStringModel(BaseModel):
    __root__: str


class RoleModel(BaseModel):
    # https://galaxy.ansible.com/docs/using/installing.html#installing-multiple-roles-from-a-file
    name: Optional[str]
    src: Optional[str]
    version: Optional[str] = "master"
    scm: Optional[Union[Literal["git"], Literal["hg"]]] = "git"

    class Config:
        title = "Role"
        extra = Extra.forbid


class IncludeModel(BaseModel):
    include: str


class RequiementsV2Model(BaseModel):
    collections: List[Union[CollectionModel, CollectionStringModel]]
    roles: List[RoleModel]

    class Config:
        title = "Requirements v2"
        extra = Extra.forbid


class RequirementsFileModel(BaseModel):
    __root__: Union[List[Union[RoleModel, IncludeModel]], RequiementsV2Model]

    class Config:
        extra = Extra.allow  # would break schema if added
        title = "Ansible Requirements Schema"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
            "examples": ["requirements.yml"],
        }
