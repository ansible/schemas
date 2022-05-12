# ajv errors

```json
[
  {
    "instancePath": "/platforms/0/networks/0",
    "keyword": "type",
    "message": "must be object",
    "params": {
      "type": "object"
    },
    "schemaPath": "#/definitions/platform-network/type"
  },
  {
    "instancePath": "/platforms/0/networks/1",
    "keyword": "type",
    "message": "must be object",
    "params": {
      "type": "object"
    },
    "schemaPath": "#/definitions/platform-network/type"
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
  negative_test/molecule/platforms_networks/molecule.yml::$.platforms[0].networks[0]: 'foo' is not of type 'object'
  negative_test/molecule/platforms_networks/molecule.yml::$.platforms[0].networks[1]: 'bar' is not of type 'object'
```
