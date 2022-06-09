# ajv errors

```json
[
  {
    "instancePath": "",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "foo"
    },
    "schemaPath": "#/additionalProperties"
  },
  {
    "instancePath": "/write_list",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/write_list/type"
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
      "filename": "negative_test/.config/ansible-lint.yml",
      "path": "$",
      "message": "Additional properties are not allowed ('foo' was unexpected)",
      "has_sub_errors": false
    },
    {
      "filename": "negative_test/.config/ansible-lint.yml",
      "path": "$.write_list",
      "message": "'foo' is not of type 'array'",
      "has_sub_errors": false
    }
  ]
}
```
