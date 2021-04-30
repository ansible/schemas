# Used to generate JSON Validations chema for requirements.
from enum import Enum
from typing import List, Mapping, Optional

import requests
from pydantic import BaseModel, Extra, Field

from . import consts


class CollectionModel(BaseModel):
    __root__: str

    class Config:
        extra = Extra.forbid


class CollectionVersionConstraintModel(BaseModel):
    __root__: str

    class Config:
        extra = Extra.forbid


spdx_licenses = []
SPDX_URL = (
    "https://raw.githubusercontent.com/spdx/license-list-data/master/json/licenses.json"
)
for lic in requests.get(SPDX_URL).json()['licenses']:
    if not lic.get('isDeprecatedLicenseId', False):
        spdx_licenses.append(lic['licenseId'])
# https://spdx.org/licenses/
args = {v: v for v in sorted(spdx_licenses)}
spdxEnum = Enum("SPDXLicenseEnum", args)  # type: ignore


class SPDXLicense(BaseModel):
    __root__: spdxEnum


class GalaxyFileModel(BaseModel):
    # https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespaces
    namespace: str = Field(regex=r"[a-z][a-z0-9_]+", min_length=2)
    name: str = Field(regex=r"[a-z][a-z0-9_]+", min_length=2)
    # https://galaxy.ansible.com/docs/contributing/version.html?highlight=version#versioning-content
    # https://semver.org/#is-there-a-suggested-regular-expression-regex-to-check-a-semver-string
    version: str = Field(
        regex=r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$",
        min_length=5,
    )
    readme: str
    authors: List[str]
    description: str
    license: Optional[List[SPDXLicense]]
    license_file: Optional[str]
    tags: Optional[List[str]]
    dependencies: Optional[Mapping[CollectionModel, CollectionVersionConstraintModel]]
    repository: Optional[str]
    documentation: Optional[str]
    homepage: Optional[str]
    issues: Optional[str]
    build_ignore: Optional[List[str]]

    class Config:
        extra = Extra.forbid
        title = "Ansible galaxy.yml Schema"
        schema_extra = {"$schema": consts.META_SCHEMA_URI, "examples": ["galaxy.yml"]}
