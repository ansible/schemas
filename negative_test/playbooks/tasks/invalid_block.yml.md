# ajv errors

```json
[
  {
    "instancePath": "/0",
    "keyword": "not",
    "message": "must NOT be valid",
    "params": {},
    "schemaPath": "#/not"
  },
  {
    "instancePath": "/0/block",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/block/type"
  },
  {
    "instancePath": "/0",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/items/anyOf"
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
  negative_test/playbooks/tasks/invalid_block.yml::$[0]: {'block': {}} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: {'block': {}} should not be valid under {'required': ['block']}
```
