# ajv errors

```json
[
  {
    "instancePath": "/0/loop",
    "keyword": "type",
    "message": "must be string,array",
    "params": {
      "type": [
        "string",
        "array"
      ]
    },
    "schemaPath": "#/properties/loop/type"
  },
  {
    "instancePath": "/0",
    "keyword": "required",
    "message": "must have required property 'block'",
    "params": {
      "missingProperty": "block"
    },
    "schemaPath": "#/required"
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
  negative_test/playbooks/tasks/loop2.yml::$[0]: {'ansible.builtin.debug': {'var': 'item'}, 'loop': 123} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: 'block' is a required property
```
