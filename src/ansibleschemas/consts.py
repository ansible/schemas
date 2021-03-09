import subprocess

# That is http:// on purpose and not https, read
# https://github.com/ajv-validator/ajv/issues/1104
META_SCHEMA_URI = "http://json-schema.org/draft-07/schema"


# I was told the vscode does not support JSON Schema 2019-09 and 2020-12, but
# only draft-07
# Read https://json-schema.org/specification-links.html
# https://json-schema.org/draft-07/schema
# https://json-schema.org/draft/2019-09/schema

SCHEMA_BASE_URI = "https://raw.githubusercontent.com/ansible-community/schemas/main/f"


# Revision is used to track changes made to our schema, for start it is based
# on number of commits being made.
_commits = subprocess.check_output(
    ["git", "rev-list", "--all", "--count", "main"], universal_newlines=True
)
REVISION = "r%s" % _commits
