# Used to generate JSON Validations chema for requirements.
from pydantic import BaseModel

from . import consts

# import META_SCHEMA_URI


class VarsModel(BaseModel):
    class Config:
        title = "Ansible Vars Schema"

        schema_extra = {
            "$schema": consts.META_SCHEMA_URI,
        }
