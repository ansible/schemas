# ajv errors

```json
[
  {
    "instancePath": "/0/with_items",
    "keyword": "pattern",
    "message": "must match pattern \"^\\{\\{.*\\}\\}$\"",
    "params": {
      "pattern": "^\\{\\{.*\\}\\}$"
    },
    "schemaPath": "#/definitions/full-jinja/pattern"
  },
  {
    "instancePath": "/0/with_items",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/with_items/anyOf/1/type"
  },
  {
    "instancePath": "/0/with_items",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/properties/with_items/anyOf"
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
  negative_test/playbooks/tasks/with_items_untemplated_string.yml::$[0]: {'command': 'echo 123', 'with_items': 'foobar'} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: 'block' is a required property
```
