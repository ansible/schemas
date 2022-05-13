# ajv errors

```json
[
  {
    "instancePath": "/0/no_log",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/oneOf/0/type"
  },
  {
    "instancePath": "/0/no_log",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/oneOf/1/type"
  },
  {
    "instancePath": "/0/no_log",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/definitions/full-jinja/type"
  },
  {
    "instancePath": "/0/no_log",
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
    "instancePath": "/0/no_log",
    "keyword": "type",
    "message": "must be boolean",
    "params": {
      "type": "boolean"
    },
    "schemaPath": "#/oneOf/0/type"
  },
  {
    "instancePath": "/0/no_log",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/oneOf/1/type"
  },
  {
    "instancePath": "/0/no_log",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/definitions/full-jinja/type"
  },
  {
    "instancePath": "/0/no_log",
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
  negative_test/playbooks/tasks/no_log_number.yml::$[0]: {'ansible.builtin.debug': {'msg': 'foo'}, 'no_log': 123} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: 'block' is a required property
```
