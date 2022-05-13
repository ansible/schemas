# ajv errors

```json
[
  {
    "instancePath": "/0/ansible.builtin.import_playbook",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/properties/ansible.builtin.import_playbook/type"
  },
  {
    "instancePath": "/0",
    "keyword": "not",
    "message": "must NOT be valid",
    "params": {},
    "schemaPath": "#/not"
  },
  {
    "instancePath": "/0",
    "keyword": "required",
    "message": "must have required property 'hosts'",
    "params": {
      "missingProperty": "hosts"
    },
    "schemaPath": "#/required"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "ansible.builtin.import_playbook"
    },
    "schemaPath": "#/additionalProperties"
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
  negative_test/playbooks/import_playbook.yml::$[0]: {'ansible.builtin.import_playbook': {}} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: Additional properties are not allowed ('ansible.builtin.import_playbook' was unexpected)
```
