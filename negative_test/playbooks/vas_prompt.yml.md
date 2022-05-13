# ajv errors

```json
[
  {
    "instancePath": "/0",
    "keyword": "required",
    "message": "must have required property 'ansible.builtin.import_playbook'",
    "params": {
      "missingProperty": "ansible.builtin.import_playbook"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/required"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "hosts"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "vars_prompt"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0/vars_prompt/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "tags"
    },
    "schemaPath": "#/definitions/vars_prompt/additionalProperties"
  },
  {
    "instancePath": "/0",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/items/anyOf"
  }
]
```

# check-jsonschema

stdout:

```json
{
  "status": "fail",
  "errors": [
    {
      "filename": "negative_test/playbooks/vas_prompt.yml",
      "path": "$[0]",
      "message": "{'hosts': 'localhost', 'vars_prompt': [{'name': 'username', 'prompt': 'What is your username?', 'private': False, 'tags': ['foo']}]} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "Additional properties are not allowed ('hosts', 'vars_prompt' were unexpected)"
      }
    }
  ]
}
```
