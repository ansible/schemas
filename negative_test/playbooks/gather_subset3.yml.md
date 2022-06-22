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
    "schemaPath": "#/oneOf/0/required"
  },
  {
    "instancePath": "/0",
    "keyword": "required",
    "message": "must have required property 'import_playbook'",
    "params": {
      "missingProperty": "import_playbook"
    },
    "schemaPath": "#/oneOf/1/required"
  },
  {
    "instancePath": "/0",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/oneOf"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "hosts"
    },
    "schemaPath": "#/additionalProperties"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "gather_subset"
    },
    "schemaPath": "#/additionalProperties"
  },
  {
    "instancePath": "/0",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "tasks"
    },
    "schemaPath": "#/additionalProperties"
  },
  {
    "instancePath": "/0/gather_subset/0",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/properties/gather_subset/items/anyOf/0/type"
  },
  {
    "instancePath": "/0/gather_subset/0",
    "keyword": "enum",
    "message": "must be equal to one of the allowed values",
    "params": {
      "allowedValues": [
        "all",
        "min",
        "hardware",
        "network",
        "virtual",
        "ohai",
        "facter"
      ]
    },
    "schemaPath": "#/properties/gather_subset/items/anyOf/0/enum"
  },
  {
    "instancePath": "/0/gather_subset/0",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/properties/gather_subset/items/anyOf/1/type"
  },
  {
    "instancePath": "/0/gather_subset/0",
    "keyword": "enum",
    "message": "must be equal to one of the allowed values",
    "params": {
      "allowedValues": [
        "!all",
        "!min",
        "!hardware",
        "!network",
        "!virtual",
        "!ohai",
        "!facter"
      ]
    },
    "schemaPath": "#/properties/gather_subset/items/anyOf/1/enum"
  },
  {
    "instancePath": "/0/gather_subset/0",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/properties/gather_subset/items/anyOf"
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
      "filename": "negative_test/playbooks/gather_subset3.yml",
      "path": "$[0]",
      "message": "{'hosts': 'localhost', 'gather_subset': [1], 'tasks': [{'ansible.builtin.debug': {'msg': 'foo'}}]} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$[0]",
        "message": "'gather_subset', 'hosts', 'tasks' do not match any of the regexes: '^(ansible\\\\.builtin\\\\.)?import_playbook$', 'name', 'tags', 'vars'"
      },
      "sub_errors": [
        {
          "path": "$[0]",
          "message": "'gather_subset', 'hosts', 'tasks' do not match any of the regexes: '^(ansible\\\\.builtin\\\\.)?import_playbook$', 'name', 'tags', 'vars'"
        },
        {
          "path": "$[0]",
          "message": "{'hosts': 'localhost', 'gather_subset': [1], 'tasks': [{'ansible.builtin.debug': {'msg': 'foo'}}]} is not valid under any of the given schemas"
        },
        {
          "path": "$[0]",
          "message": "'ansible.builtin.import_playbook' is a required property"
        },
        {
          "path": "$[0]",
          "message": "'import_playbook' is a required property"
        },
        {
          "path": "$[0].gather_subset[0]",
          "message": "1 is not valid under any of the given schemas"
        },
        {
          "path": "$[0].gather_subset[0]",
          "message": "1 is not one of ['all', 'min', 'hardware', 'network', 'virtual', 'ohai', 'facter']"
        },
        {
          "path": "$[0].gather_subset[0]",
          "message": "1 is not of type 'string'"
        },
        {
          "path": "$[0].gather_subset[0]",
          "message": "1 is not one of ['!all', '!min', '!hardware', '!network', '!virtual', '!ohai', '!facter']"
        },
        {
          "path": "$[0].gather_subset[0]",
          "message": "1 is not of type 'string'"
        }
      ]
    }
  ]
}
```
