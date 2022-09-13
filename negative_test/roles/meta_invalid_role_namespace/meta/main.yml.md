# ajv errors

```json
[
  {
    "instancePath": "/galaxy_info/namespace",
    "keyword": "pattern",
    "message": "must match pattern \"^[a-z][a-z0-9_]+$\"",
    "params": {
      "pattern": "^[a-z][a-z0-9_]+$"
    },
    "schemaPath": "#/properties/namespace/pattern"
  },
  {
    "instancePath": "/galaxy_info",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "min_ansible_version"
    },
    "schemaPath": "#/additionalProperties"
  },
  {
    "instancePath": "/galaxy_info",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "namespace"
    },
    "schemaPath": "#/additionalProperties"
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
      "filename": "negative_test/roles/meta_invalid_role_namespace/meta/main.yml",
      "path": "$",
      "message": "{'galaxy_info': {'description': 'foo', 'min_ansible_version': '2.9', 'namespace': 'foo-bar', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$.galaxy_info",
        "message": "Additional properties are not allowed ('min_ansible_version', 'namespace' were unexpected)"
      },
      "sub_errors": [
        {
          "path": "$.galaxy_info.namespace",
          "message": "'foo-bar' does not match '^[a-z][a-z0-9_]+$'"
        },
        {
          "path": "$.galaxy_info",
          "message": "Additional properties are not allowed ('min_ansible_version', 'namespace' were unexpected)"
        }
      ]
    }
  ],
  "parse_errors": []
}
```
