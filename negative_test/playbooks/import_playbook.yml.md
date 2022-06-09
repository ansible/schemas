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
    "schemaPath": "#/patternProperties/%5E(ansible%5C.builtin%5C.)%3Fimport_playbook%24/type"
  },
  {
    "instancePath": "/0",
    "keyword": "not",
    "message": "must NOT be valid",
    "params": {},
    "schemaPath": "#/allOf/0/not"
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
      "filename": "negative_test/playbooks/import_playbook.yml",
      "path": "$[0]",
      "message": "{'ansible.builtin.import_playbook': {}} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "Additional properties are not allowed ('ansible.builtin.import_playbook' was unexpected)"
      }
    }
  ]
}
```
