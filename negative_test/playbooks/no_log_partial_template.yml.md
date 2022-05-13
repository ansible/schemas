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
    "instancePath": "/0/tasks/0/no_log",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/oneOf/0/type"
  },
  {
    "instancePath": "/0/tasks/0/no_log",
    "keyword": "pattern",
    "message": "must match pattern \"^\\{\\{.*\\}\\}$\"",
    "params": {
      "pattern": "^\\{\\{.*\\}\\}$"
    },
    "schemaPath": "#/definitions/full-jinja/pattern"
  },
  {
    "instancePath": "/0/tasks/0/no_log",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/oneOf"
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
    "instancePath": "/0/tasks/0/no_log",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/oneOf/0/type"
  },
  {
    "instancePath": "/0/tasks/0/no_log",
    "keyword": "pattern",
    "message": "must match pattern \"^\\{\\{.*\\}\\}$\"",
    "params": {
      "pattern": "^\\{\\{.*\\}\\}$"
    },
    "schemaPath": "#/definitions/full-jinja/pattern"
  },
  {
    "instancePath": "/0/tasks/0/no_log",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/oneOf"
  },
  {
    "instancePath": "/0/tasks/0",
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
  negative_test/playbooks/no_log_partial_template.yml::$[0]: {'hosts': 'localhost', 'vars': {'some_var': True}, 'tasks': [{'ansible.builtin.debug': {'msg': 'foo'}, 'no_log': 'foo-{{ some_var }}'}]} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: Additional properties are not allowed ('hosts', 'tasks' were unexpected)
```
