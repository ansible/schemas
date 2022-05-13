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
      "additionalProperty": "tasks"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0/tasks/0/failed_when",
    "keyword": "type",
    "message": "must be string,boolean",
    "params": {
      "type": [
        "string",
        "boolean"
      ]
    },
    "schemaPath": "#/properties/failed_when/type"
  },
  {
    "instancePath": "/0/tasks/0",
    "keyword": "required",
    "message": "must have required property 'block'",
    "params": {
      "missingProperty": "block"
    },
    "schemaPath": "#/required"
  },
  {
    "instancePath": "/0/tasks/0",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/items/anyOf"
  },
  {
    "instancePath": "/0/tasks/1/failed_when",
    "keyword": "type",
    "message": "must be string,boolean",
    "params": {
      "type": [
        "string",
        "boolean"
      ]
    },
    "schemaPath": "#/properties/failed_when/type"
  },
  {
    "instancePath": "/0/tasks/1",
    "keyword": "required",
    "message": "must have required property 'block'",
    "params": {
      "missingProperty": "block"
    },
    "schemaPath": "#/required"
  },
  {
    "instancePath": "/0/tasks/1",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/items/anyOf"
  },
  {
    "instancePath": "/0/tasks/2/failed_when",
    "keyword": "type",
    "message": "must be string,boolean",
    "params": {
      "type": [
        "string",
        "boolean"
      ]
    },
    "schemaPath": "#/properties/failed_when/type"
  },
  {
    "instancePath": "/0/tasks/2",
    "keyword": "required",
    "message": "must have required property 'block'",
    "params": {
      "missingProperty": "block"
    },
    "schemaPath": "#/required"
  },
  {
    "instancePath": "/0/tasks/2",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/items/anyOf"
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

stderr:

```
Schema validation errors were encountered.
```

stdout:

```
  negative_test/playbooks/invalid-failed-when.yml::$[0]: {'hosts': 'localhost', 'tasks': [{'debug': {'msg': 'failed_when should not accept numeric'}, 'failed_when': 123}, {'debug': {'msg': 'failed_when should not accept sequence'}, 'failed_when': ['foo', 'bar']}, {'debug': {'msg': 'failed_when should not accept map'}, 'failed_when': {}}]} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: Additional properties are not allowed ('hosts', 'tasks' were unexpected)
```
