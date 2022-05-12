# ajv errors

```json
[
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/anyOf/0/type"
  },
  {
    "instancePath": "",
    "keyword": "required",
    "message": "must have required property 'collections'",
    "params": {
      "missingProperty": "collections"
    },
    "schemaPath": "#/anyOf/0/required"
  },
  {
    "instancePath": "",
    "keyword": "required",
    "message": "must have required property 'roles'",
    "params": {
      "missingProperty": "roles"
    },
    "schemaPath": "#/anyOf/1/required"
  },
  {
    "instancePath": "",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/anyOf"
  },
  {
    "instancePath": "",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "foo"
    },
    "schemaPath": "#/additionalProperties"
  },
  {
    "instancePath": "",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/anyOf"
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
  negative_test/reqs3/meta/requirements.yml::$: {'foo': 'bar'} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $: {'foo': 'bar'} is not of type 'array'
```
