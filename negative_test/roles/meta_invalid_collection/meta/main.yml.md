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

# check-jsonschema

stderr:

```
  negative_test/roles/meta_invalid_collection/meta/main.yml::$: {'collections': ['foo'], 'galaxy_info': {'description': 'foo', 'license': 'bar', 'min_ansible_version': '2.10', 'platforms': [{'name': 'Fedora', 'versions': ['all']}]}} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $: {'collections': ['foo'], 'galaxy_info': {'description': 'foo', 'license': 'bar', 'min_ansible_version': '2.10', 'platforms': [{'name': 'Fedora', 'versions': ['all']}]}} is not of type 'null'
```

stdout:

```
Schema validation errors were encountered.
```
