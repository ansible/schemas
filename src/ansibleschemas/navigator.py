# Used to generate JSON Validations chema for ansible-lint config files
# https://github.com/ansible-community/ansible-lint/blob/master/.ansible-lint
from typing import List, Mapping, Optional

from pydantic import BaseModel, Extra
from pydantic.fields import Field

from . import consts


class AnsibleModel(BaseModel):
    config: str  # tododo "/tmp/ansible.cfg"
    cmdline: str  # tododo "--forks 15"
    inventories: List[str]
    # tododo "- /tmp/test_inventory.yml"
    playbook: str  # tododo "/tmp/test_playbook.yml"

    class Config:
        extra = Extra.forbid


class AnsibleRunnerModel(BaseModel):
    artifact_dir: str = Field(alias="artifact-dir")  # todoo "/tmp/test1"
    rotate_artifacts_count: int = Field(alias="rotate-artifacts-count")  # todoo "10"
    timeout: int  # todoo 300

    class Config:
        extra = Extra.forbid


class ColorModel(BaseModel):
    enable: bool  # False
    osc4: bool  # False

    class Config:
        extra = Extra.forbid


class DocumentationModel(BaseModel):
    class PluginModel(BaseModel):
        name: str  # tododo "shell"
        type: str  # tododo "become"

        class Config:
            extra = Extra.forbid

    plugin: PluginModel

    class Config:
        extra = Extra.forbid


class EditorModel(BaseModel):
    command: str  # tododo "vim_from_setting"
    console: Optional[bool]

    class Config:
        extra = Extra.forbid


class ExecModel(BaseModel):
    shell: Optional[bool]
    command: str  # tododo "/bin/foo"

    class Config:
        extra = Extra.forbid


class ExecutionEnvironmentModel(BaseModel):
    class EnvironmentVariablesModel(BaseModel):
        pass_: List[str] = Field(alias="pass")
        set: Optional[Mapping[str, str]]

        class Config:
            extra = Extra.forbid

    class VolumeMountsModel(BaseModel):
        src: str  # tododo "/test1"
        dest: str  # tododo "/test1"
        label: str  # tododo "Z"

        class Config:
            extra = Extra.forbid

    container_engine: str = Field(alias="container-engine")  # tododo "podman"
    enabled: bool
    environment_variables: EnvironmentVariablesModel = Field(
        alias="environment-variables"
    )
    image: str  # tododo "test_image:latest"
    pull_policy: str = Field(alias="pull-policy")  # tododo "never"
    volume_mounts: List[VolumeMountsModel] = Field(alias="volume-mounts")
    container_options: List[str] = Field(alias="container-options")  # tododo
    # - "--net=host"

    class Config:
        extra = Extra.forbid


class LoggingModel(BaseModel):
    level: str  # tododo "critical"
    append: Optional[bool]
    file: str  # tododo "/tmp/log.txt"

    class Config:
        extra = Extra.forbid


class PlaybookArtifactModel(BaseModel):
    enable: bool
    replay: str  # tododo "/tmp/test_artifact.json"
    save_as: str = Field(alias="save-as")  # tododo "/tmp/test_artifact.json"

    class Config:
        extra = Extra.forbid


class AnsibleNavigatorModel(BaseModel):
    ansible: AnsibleModel
    ansible_runner: AnsibleRunnerModel = Field(alias="ansible-runner")
    app: str  # tododo "run"
    collection_doc_cache_path: str = Field(alias="collection-doc-cache-path")
    color: ColorModel
    documentation: DocumentationModel
    editor: EditorModel
    exec: ExecModel
    execution_environment: ExecutionEnvironmentModel = Field(
        alias="execution-environment"
    )
    help_config: Optional[bool] = Field(alias="help-config")
    help_doc: Optional[bool] = Field(alias="help-doc")
    help_inventory: Optional[bool] = Field(alias="help-inventory")
    help_playbook: Optional[bool] = Field(alias="help-playbook")
    inventory_columns: List[str] = Field(alias="inventory-columns")  # tododo
    # - ansible_network_os
    # - ansible_network_cli_ssh_type
    # - ansible_connection
    logging: LoggingModel
    mode: str  # tododo "stdout"
    playbook_artifact: PlaybookArtifactModel = Field(alias="playbook-artifact")

    class Config:
        extra = Extra.forbid


class NavigatorModel(BaseModel):
    ansible_navigator: AnsibleNavigatorModel = Field(alias="ansible-navigator")

    class Config:
        extra = Extra.forbid
        title = "Ansible-Navigator Configuration Schema"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
            "examples": ["ansible-navigator.yml"],
        }
