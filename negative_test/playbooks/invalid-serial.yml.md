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
      "additionalProperty": "serial"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0/serial",
    "keyword": "type",
    "message": "must be integer",
    "params": {
      "type": "integer"
    },
    "schemaPath": "#/properties/serial/anyOf/0/type"
  },
  {
    "instancePath": "/0/serial",
    "keyword": "pattern",
    "message": "must match pattern \"^\\d+\\.?\\d*%?$\"",
    "params": {
      "pattern": "^\\d+\\.?\\d*%?$"
    },
    "schemaPath": "#/properties/serial/anyOf/1/pattern"
  },
  {
    "instancePath": "/0/serial",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/serial/anyOf/2/type"
  },
  {
    "instancePath": "/0/serial",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/properties/serial/anyOf"
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
      "filename": "negative_test/playbooks/invalid-serial.yml",
      "path": "$[0]",
      "message": "{'hosts': 'localhost', 'serial': '10%BAD'} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "Additional properties are not allowed ('hosts', 'serial' were unexpected)"
      }
    }
  ]
}
```
