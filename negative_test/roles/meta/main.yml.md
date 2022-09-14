# ajv errors

```json
[
  {
    "instancePath": "/galaxy_info/galaxy_tags",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/galaxy_tags/type"
  },
  {
    "instancePath": "",
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
      "filename": "negative_test/roles/meta/main.yml",
      "path": "$.galaxy_info.galaxy_tags",
      "message": "'database' is not of type 'array'",
      "has_sub_errors": false
    }
  ],
  "parse_errors": []
}
```
