# ajv errors

```json
[
  {
    "instancePath": "/0/tags",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/properties/tags/anyOf/0/type"
  },
  {
    "instancePath": "/0/tags",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/tags/anyOf/1/type"
  },
  {
    "instancePath": "/0/tags",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/properties/tags/anyOf"
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
    "instancePath": "/0/tags",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/properties/tags/anyOf/0/type"
  },
  {
    "instancePath": "/0/tags",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/tags/anyOf/1/type"
  },
  {
    "instancePath": "/0/tags",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/properties/tags/anyOf"
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
  negative_test/playbooks/tasks/tags-mapping.yml::$[0]: {'ansible.builtin.debug': {'msg': 'foo'}, 'tags': {}} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $[0]: 'block' is a required property
```
