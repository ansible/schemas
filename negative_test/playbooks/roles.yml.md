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
      "additionalProperty": "roles"
    },
    "schemaPath": "#/definitions/ansible.builtin.import_playbook/additionalProperties"
  },
  {
    "instancePath": "/0/roles",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/roles/type"
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
      "filename": "negative_test/playbooks/roles.yml",
      "path": "$[0]",
      "message": "{'hosts': 'localhost', 'roles': 'xxx'} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "'hosts', 'roles' do not match any of the regexes: '^(ansible\\\\.builtin\\\\.)?import_playbook$', 'name', 'vars'"
      }
    }
  ]
}
```
