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
    "instancePath": "/galaxy_info",
    "keyword": "required",
    "message": "must have required property 'standalone'",
    "params": {
      "missingProperty": "standalone"
    },
    "schemaPath": "#/then/required"
  },
  {
    "instancePath": "/galaxy_info",
    "keyword": "required",
    "message": "must have required property 'min_ansible_version'",
    "params": {
      "missingProperty": "min_ansible_version"
    },
    "schemaPath": "#/then/required"
  },
  {
    "instancePath": "/galaxy_info",
    "keyword": "if",
    "message": "must match \"then\" schema",
    "params": {
      "failingKeyword": "then"
    },
    "schemaPath": "#/if"
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
      "filename": "negative_test/roles/meta_invalid_collection/meta/main.yml",
      "path": "$.collections[0]",
      "message": "'foo' does not match '^[a-z_]+\\\\.[a-z_]+$'",
      "has_sub_errors": false
    },
    {
      "filename": "negative_test/roles/meta_invalid_collection/meta/main.yml",
      "path": "$.galaxy_info",
      "message": "'standalone' is a required property",
      "has_sub_errors": false
    },
    {
      "filename": "negative_test/roles/meta_invalid_collection/meta/main.yml",
      "path": "$.galaxy_info",
      "message": "'min_ansible_version' is a required property",
      "has_sub_errors": false
    }
  ],
  "parse_errors": []
}
```
