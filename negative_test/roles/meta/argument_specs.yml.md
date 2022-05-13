# ajv errors

```json
[
  {
    "instancePath": "/argument_specs/main",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "foo"
    },
    "schemaPath": "#/additionalProperties"
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
  negative_test/roles/meta/argument_specs.yml::$.argument_specs.main: Additional properties are not allowed ('foo' was unexpected)
```
