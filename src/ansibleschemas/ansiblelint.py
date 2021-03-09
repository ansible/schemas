# Used to generate JSON Validations chema for ansible-lint config files
# https://github.com/ansible-community/ansible-lint/blob/master/.ansible-lint
from typing import Any, List, Mapping, Optional

from pydantic import BaseModel, Extra

from . import consts


class AnsibleLintModel(BaseModel):
    exclude_paths: Optional[List[str]]
    extra_vars: Optional[Mapping[str, Any]]
    loop_var_prefix: Optional[str]
    mock_modules: Optional[List[str]]
    mock_roles: Optional[List[str]]
    offline: Optional[bool] = False
    parseable: Optional[bool] = True
    quiet: Optional[bool] = True
    rulesdir: Optional[List[str]]
    skip_action_validation: Optional[bool] = False
    skip_list: Optional[List[str]]
    tags: Optional[List[str]]
    use_default_rules: Optional[bool] = True
    verbosity: Optional[int] = 0
    warn_list: Optional[List[str]]

    class Config:
        extra = Extra.forbid
        title = f"Ansible-lint Configuration Schema {consts.REVISION}"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
        }
