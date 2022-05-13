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
      "additionalProperty": "pre_tasks"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "post_tasks"
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
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "handlers"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0/handlers",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/type"
  },
  {
    "instancePath": "/0/post_tasks",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/type"
  },
  {
    "instancePath": "/0/pre_tasks",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/type"
  },
  {
    "instancePath": "/0/tasks",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/type"
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
      "filename": "negative_test/playbooks/tasks.yml",
      "path": "$[0]",
      "message": "{'hosts': 'localhost', 'pre_tasks': 'foo', 'post_tasks': {}, 'tasks': 1, 'handlers': 1.0} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "Additional properties are not allowed ('handlers', 'hosts', 'post_tasks', 'pre_tasks', 'tasks' were unexpected)"
      }
    }
  ]
}
```
