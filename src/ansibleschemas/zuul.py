# Used to generate JSON Validations schema for Zuul config files.
from typing import Any, List, Mapping, Optional, Union

from pydantic import BaseModel, Extra, Field

from . import consts


class PipelineModel(BaseModel):
    jobs: Optional[List[Any]]

    class Config:
        extra = Extra.forbid


class ProjectTemplateModel(BaseModel):
    name: str
    description: Optional[str]
    vars: Optional[Mapping[str, Any]]
    # For the moment we hardcode common pipeline names, until we figure out
    # a way to distinguish pipelines from other properties.
    post: Optional[PipelineModel]
    release: Optional[PipelineModel]
    check: Optional[PipelineModel]
    gate: Optional[PipelineModel]

    class Config:
        extra = Extra.forbid


class ProjectModel(ProjectTemplateModel):
    templates: Optional[List[str]]

    class Config:
        extra = Extra.forbid


class JobModel(BaseModel):
    # based on https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#play
    name: str
    description: Optional[str]
    pre_run: Optional[str] = Field(alias="pre-run")
    post_run: Optional[str] = Field(alias="post-run")
    run: Optional[str]
    nodeset: Optional[Any]
    parent: Optional[str]
    vars: Optional[Mapping[str, Any]]
    files: Optional[Union[str, List[str]]]
    override_checkout: Optional[str] = Field(alias="override-checkout")
    success_url: Optional[str] = Field(alias="success-url")

    class Config:
        extra = Extra.forbid


class JobEntry(BaseModel):
    # based on https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#play
    job: JobModel

    class Config:
        extra = Extra.forbid


class ProjectTemplateEntry(BaseModel):
    # based on https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#play
    project_template: ProjectTemplateModel = Field(alias="project-template")

    class Config:
        extra = Extra.forbid


class ProjectEntry(BaseModel):
    # based on https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html#play
    project: ProjectModel

    class Config:
        extra = Extra.forbid


class ZuulConfigModel(BaseModel):
    __root__: List[Union[JobEntry, ProjectEntry, ProjectTemplateEntry]]

    class Config:
        extra = Extra.forbid
        title = "Zuul Config Schema"
        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
        }
