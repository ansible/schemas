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
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/oneOf/0/required"
  },
  {
    "instancePath": "/0",
    "keyword": "required",
    "message": "must have required property 'import_playbook'",
    "params": {
      "missingProperty": "import_playbook"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/oneOf/1/required"
  },
  {
    "instancePath": "/0",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/oneOf"
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
      "additionalProperty": "environment"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0/environment",
    "keyword": "type",
    "message": "must be object",
    "params": {
      "type": "object"
    },
    "schemaPath": "#/anyOf/0/type"
  },
  {
    "instancePath": "/0/environment",
    "keyword": "pattern",
    "message": "must match pattern \"^\\{\\{.*\\}\\}$\"",
    "params": {
      "pattern": "^\\{\\{.*\\}\\}$"
    },
    "schemaPath": "#/definitions/full-jinja/pattern"
  },
  {
    "instancePath": "/0/environment",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/anyOf"
  },
  {
    "instancePath": "/0",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/items/oneOf"
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
      "filename": "negative_test/playbooks/environment.yml",
      "path": "$[0]",
      "message": "{'hosts': 'localhost', 'environment': '{{ foo }}-123'} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "'environment', 'hosts' do not match any of the regexes: '^(ansible\\\\.builtin\\\\.)?import_playbook$', 'name', 'vars'"
      }
    }
  ]
}
```
