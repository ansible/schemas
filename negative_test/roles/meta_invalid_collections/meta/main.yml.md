# ajv errors

```json
[
  {
    "instancePath": "/collections/0",
    "keyword": "pattern",
    "message": "must match pattern \"^[a-z_]+\\.[a-z_]+$\"",
    "params": {
      "pattern": "^[a-z_]+\\.[a-z_]+$"
    },
    "schemaPath": "#/$defs/collections/items/pattern"
  },
  {
    "instancePath": "/collections/0",
    "keyword": "pattern",
    "message": "must match pattern \"^[a-z_]+\\.[a-z_]+$\"",
    "params": {
      "pattern": "^[a-z_]+\\.[a-z_]+$"
    },
    "schemaPath": "#/$defs/collections/items/pattern"
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
      "filename": "negative_test/roles/meta_invalid_collections/meta/main.yml",
      "path": "$",
      "message": "{'collections': ['FOO.BAR'], 'galaxy_info': {'description': 'foo', 'license': 'bar', 'min_ansible_version': '2.10', 'platforms': [{'name': 'Fedora', 'versions': ['all']}]}} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$.galaxy_info",
        "message": "Additional properties are not allowed ('min_ansible_version' was unexpected)"
      },
      "sub_errors": [
        {
          "path": "$.collections[0]",
          "message": "'FOO.BAR' does not match '^[a-z_]+\\\\.[a-z_]+$'"
        },
        {
          "path": "$.collections[0]",
          "message": "'FOO.BAR' does not match '^[a-z_]+\\\\.[a-z_]+$'"
        },
        {
          "path": "$.galaxy_info",
          "message": "Additional properties are not allowed ('min_ansible_version' was unexpected)"
        }
      ]
    }
  ],
  "parse_errors": []
}
```
