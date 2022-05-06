# ajv errors

```json
[
  {
    "instancePath": "",
    "keyword": "type",
    "message": "must be null",
    "params": {
      "type": "null"
    },
    "schemaPath": "#/anyOf/0/type"
  },
  {
    "instancePath": "/collections/0",
    "keyword": "pattern",
    "message": "must match pattern \"^[a-z_]+\\.[a-z_]+$\"",
    "params": {
      "pattern": "^[a-z_]+\\.[a-z_]+$"
    },
    "schemaPath": "#/anyOf/1/properties/collections/items/pattern"
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
