# Used to generate JSON Validations Schema for requirements.
from typing import Any, List, Mapping, Optional, Union

from pydantic import BaseModel, Extra, Field, create_model

from . import consts
from .api import ansible_modules


def cleanup_schema(schema: Any) -> None:
    """Remove generated titles as they make the schema bulky."""
    # https://github.com/samuelcolvin/pydantic/discussions/2495#discussioncomment-450329
    # schema.pop('title', None)  # remove title of model
    # pylint: disable=unused-variable
    for field_name, field_props in schema.get('properties', {}).items():
        field_props.pop('title', None)  # remove title of fields


class _SharedModel(BaseModel):
    # Properties shared between Play, Role, Block and Task
    any_errors_fatal: Optional[bool]
    become: Optional[bool]
    become_exe: Optional[str]
    become_flags: Optional[str]
    become_method: Optional[str]
    become_user: Optional[str]
    check_mode: Optional[bool]
    collections: Optional[List[str]]
    connection: Optional[str]
    debugger: Optional[str]
    diff: Optional[bool]
    environment: Optional[Mapping[str, str]]
    ignore_errors: Optional[bool]
    ignore_unreachable: Optional[bool]
    module_defaults: Optional[Any]
    name: Optional[str]  # SHOULD BE REQUIRED
    no_log: Optional[bool]
    port: Optional[int]
    remote_user: Optional[str]
    run_once: Optional[bool]
    tags: Optional[Union[str, List[str]]]
    throttle: Optional[int]
    timeout: Optional[int]
    vars: Optional[Mapping[str, Any]]
    when: Optional[Union[str, List[str]]]


class TaskModel(_SharedModel):
    action: str
    args: Optional[Mapping[str, Any]]
    async_: Optional[int] = Field(alias="async")
    changed_when: Optional[bool]
    delay: Optional[int]
    delegate_facts: Optional[bool]
    delegate_to: Optional[str]
    failed_when: Optional[str]
    local_action: Optional[str]
    notify: Optional[str]
    poll: Optional[int]
    register_: Optional[str] = Field(alias="register")
    retries: Optional[int]
    until: Optional[str]
    loop: Optional[str]
    loop_control: Optional[Any]
    # deprecated looping:
    with_items: Optional[Union[str, List[str]]]
    with_dict: Optional[Any]
    with_fileglob: Optional[Any]
    with_filetree: Optional[Any]
    with_first_found: Optional[Any]
    with_together: Optional[Any]
    with_subelements: Optional[Any]
    with_sequence: Optional[Any]
    with_random_choice: Optional[Any]
    with_lines: Optional[Any]
    with_indexed_items: Optional[Any]
    with_ini: Optional[Any]
    with_flattened: Optional[Any]
    with_inventory_hostnames: Optional[Any]

    class Config:
        extra = Extra.forbid


class BlockModel(_SharedModel):
    always: "Optional[List[Union[TaskModel, BlockModel]]]" = None
    block: "Optional[List[Union[TaskModel, BlockModel]]]" = None
    rescue: "Optional[List[Union[TaskModel, BlockModel]]]" = None
    delegate_facts: Optional[bool]
    delegate_to: Optional[str]


# https://pydantic-docs.helpmanual.io/usage/postponed_annotations/#self-referencing-models
BlockModel.update_forward_refs()

# Alternative approach of combining all modules into a single BeremothModel,
# which seems to produce ~1.1mb file.
kwargs = dict()
for module in ansible_modules():

    if module in ['copy']:
        module_sanitized = f"{module}_"
    else:
        module_sanitized = module
    # Optional is used because we only need one of them
    kwargs[module_sanitized] = (
        Optional[Mapping[str, Any]],
        Field(title=".", alias=module),
    )
kwargs['__base__'] = TaskModel  # type: ignore
# kwargs['schema_extra'] = cleanup_schema  # type: ignore

BeremothTaskModel = create_model("BeremothTaskModel", **kwargs)  # type: ignore
BeremothTaskModel.__config__.schema_extra = cleanup_schema  # type: ignore

# all_tasks_models = (TaskModel, BlockModel, *tuple(generated_tasks_models.values()))


class TasksListModel(BaseModel):
    __root__: List[Union[TaskModel, BlockModel, BeremothTaskModel]]  # type: ignore

    class Config:
        # Uncomment this once we succeed injecting all known modules to
        # the __root__ list, until then we have to ignore unknown properties.
        # extra = Extra.forbid
        title = "Ansible Tasks Schema"

        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
            "examples": ["tasks/*.yml", "handlers/*.yml"],
        }
