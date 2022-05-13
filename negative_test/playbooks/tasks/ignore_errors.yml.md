# ajv errors

```json
[
  {
    "instancePath": "/0/ignore_errors",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/oneOf/0/type"
  },
  {
    "instancePath": "/0/ignore_errors",
    "keyword": "pattern",
    "message": "must match pattern \"^\\{\\{.*\\}\\}$\"",
    "params": {
      "pattern": "^\\{\\{.*\\}\\}$"
    },
    "schemaPath": "#/definitions/full-jinja/pattern"
  },
  {
    "instancePath": "/0/ignore_errors",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/oneOf"
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
    "instancePath": "/0/ignore_errors",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/oneOf/0/type"
  },
  {
    "instancePath": "/0/ignore_errors",
    "keyword": "pattern",
    "message": "must match pattern \"^\\{\\{.*\\}\\}$\"",
    "params": {
      "pattern": "^\\{\\{.*\\}\\}$"
    },
    "schemaPath": "#/definitions/full-jinja/pattern"
  },
  {
    "instancePath": "/0/ignore_errors",
    "keyword": "oneOf",
    "message": "must match exactly one schema in oneOf",
    "params": {
      "passingSchemas": null
    },
    "schemaPath": "#/oneOf"
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
  negative_test/playbooks/tasks/ignore_errors.yml::$[0]: {'command': 'echo 123', 'vars': {'should_ignore_errors': True}, 'ignore_errors': 'should_ignore_errors'} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: 'block' is a required property
```
