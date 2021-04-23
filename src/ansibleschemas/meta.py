# Used to generate JSON Validations chema for requirements.
import sys
from collections.abc import Iterable
from enum import Enum
from typing import Any, List, Mapping, Optional, Union

from pydantic import BaseModel, Extra, Field, create_model

from . import consts
from ._galaxy import GALAXY_PLATFORMS

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module
else:
    from typing_extensions import Literal


kwargs = dict()
all_platforms = []

for platform_name, platform_versions in GALAXY_PLATFORMS.items():

    if not isinstance(platform_versions, Iterable):
        raise RuntimeError("Platforms versions are supposed to be list of strings.")

    args = {v: v for v in platform_versions}
    args['any'] = 'any'
    versionsEnum = Enum(f"{platform_name}PlatformVersionsEnum", args)  # type: ignore

    kwargs['name'] = Field(platform_name, const=True)
    kwargs['versions'] = Field("any")

    model = create_model(
        f"{platform_name}PlatformModel",
        name=(str, Field(platform_name, const=True)),
        versions=(List[versionsEnum], "any"),
    )  # type: ignore
    model.update_forward_refs()
    all_platforms.append(model)

all_platforms_tuple = tuple(all_platforms)


class GalaxyInfoModel(BaseModel):
    role_name: Optional[str] = Field(regex=r"[a-z][a-z0-9_]+", min_length=2)
    author: Optional[str] = Field(regex=r"[a-z0-9][a-z0-9_]+", min_length=2)
    description: str
    company: str
    issue_tracker_url: Optional[str]
    license: str
    min_ansible_version: str
    min_ansible_container_version: Optional[str]
    platforms: List[Union[all_platforms_tuple]]  # type: ignore
    galaxy_tags: List[str]

    class Config:
        extra = Extra.forbid


class DependencyModel(BaseModel):
    role: str
    src: Optional[str]
    # name: Union[str, HttpUrl] = Field(regex=r"[a-z][a-z0-9_]+\.[a-z0-9][a-z0-9_]+", min_length=2)
    # ^ url or galaxy namespace.rolename
    vars: Optional[Mapping[str, Any]]
    version: Optional[str]
    scm: Optional[Literal["hg", "git"]]

    class Config:
        extra = Extra.forbid


class MetaModel(BaseModel):
    galaxy_info: GalaxyInfoModel
    dependencies: Optional[List[DependencyModel]]
    # https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#using-allow-duplicates-true
    allow_duplicates: Optional[bool]

    class Config:
        extra = Extra.forbid
        title = "Ansible Meta Schema"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
        }
