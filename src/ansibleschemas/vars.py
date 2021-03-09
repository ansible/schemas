# Used to generate JSON Validations chema for requirements.
from pydantic import BaseModel

from . import consts

# import META_SCHEMA_URI


class VarsModel(BaseModel):
    class Config:
        title = f"Ansible Vars Schema {consts.REVISION}"

        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
        }
