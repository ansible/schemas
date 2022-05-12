# ajv errors

```json
[
  {
    "instancePath": "/all",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "foo"
    },
    "schemaPath": "#/definitions/special-group/additionalProperties"
  }
]
```

# check-jsonschema

stderr:

```
Schema validation errors were encountered.
```

stdout:

```
  negative_test/inventory/broken_dev_inventory.yml::$.all: Additional properties are not allowed ('foo' was unexpected)
```
