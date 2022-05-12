# ajv errors

```json
[
  {
    "instancePath": "/platforms/0/children",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/children/type"
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
  negative_test/molecule/platforms_children/molecule.yml::$.platforms[0].children: 2 is not of type 'array'
```
