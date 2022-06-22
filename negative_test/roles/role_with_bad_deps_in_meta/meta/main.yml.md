# ajv errors

```json
[
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be null",
    "params": {
      "type": "null"
    },
    "schemaPath": "#/anyOf/0/type"
  },
  {
    "instancePath": "/dependencies/0",
    "keyword": "required",
    "message": "must have required property 'role'",
    "params": {
      "missingProperty": "role"
    },
    "schemaPath": "#/anyOf/0/required"
  },
  {
    "instancePath": "/dependencies/0",
    "keyword": "required",
    "message": "must have required property 'src'",
    "params": {
      "missingProperty": "src"
    },
    "schemaPath": "#/anyOf/1/required"
  },
  {
    "instancePath": "/dependencies/0",
    "keyword": "required",
    "message": "must have required property 'name'",
    "params": {
      "missingProperty": "name"
    },
    "schemaPath": "#/anyOf/2/required"
  },
  {
    "instancePath": "/dependencies/0",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/anyOf"
  },
  {
    "instancePath": "",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/anyOf"
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
      "filename": "negative_test/roles/role_with_bad_deps_in_meta/meta/main.yml",
      "path": "$",
      "message": "{'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}, 'dependencies': [{'version': 'foo'}]} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$",
        "message": "{'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}, 'dependencies': [{'version': 'foo'}]} is not of type 'null'"
      },
      "sub_errors": [
        {
          "path": "$",
          "message": "{'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}, 'dependencies': [{'version': 'foo'}]} is not of type 'null'"
        },
        {
          "path": "$.dependencies[0]",
          "message": "{'version': 'foo'} is not valid under any of the given schemas"
        },
        {
          "path": "$.dependencies[0]",
          "message": "'role' is a required property"
        },
        {
          "path": "$.dependencies[0]",
          "message": "'src' is a required property"
        },
        {
          "path": "$.dependencies[0]",
          "message": "'name' is a required property"
        }
      ]
    }
  ]
}
```
