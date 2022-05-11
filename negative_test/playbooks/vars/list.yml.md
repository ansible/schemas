# ajv errors

```json
[
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be object",
    "params": {
      "type": "object"
    },
    "schemaPath": "#/anyOf/0/type"
  },
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be string",
    "params": {
      "type": "string"
    },
    "schemaPath": "#/anyOf/1/type"
  },
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be null",
    "params": {
      "type": "null"
    },
    "schemaPath": "#/anyOf/2/type"
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
  negative_test/playbooks/vars/list.yml::$: ['foo', 'bar'] is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $: ['foo', 'bar'] is not of type 'object'
```

stdout:

```
Schema validation errors were encountered.
```
