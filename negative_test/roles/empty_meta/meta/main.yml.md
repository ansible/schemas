# ajv errors

```json
[
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be object",
    "params": {
      "type": "object"
    },
    "schemaPath": "#/type"
  },
  {
    "instancePath": "",
    "keyword": "if",
    "message": "must match \"then\" schema",
    "params": {
      "failingKeyword": "then"
    },
    "schemaPath": "#/if"
  },
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be object",
    "params": {
      "type": "object"
    },
    "schemaPath": "#/type"
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
      "filename": "negative_test/roles/empty_meta/meta/main.yml",
      "path": "$",
      "message": "None is not of type 'object'",
      "has_sub_errors": false
    },
    {
      "filename": "negative_test/roles/empty_meta/meta/main.yml",
      "path": "$",
      "message": "None is not of type 'object'",
      "has_sub_errors": false
    }
  ],
  "parse_errors": []
}
```
