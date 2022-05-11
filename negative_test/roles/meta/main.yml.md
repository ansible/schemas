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
    "instancePath": "/galaxy_info/galaxy_tags",
    "keyword": "type",
    "message": "must be array",
    "params": {
      "type": "array"
    },
    "schemaPath": "#/properties/galaxy_tags/type"
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
  negative_test/roles/meta/main.yml::$: {'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'galaxy_tags': 'database', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $: {'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'galaxy_tags': 'database', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not of type 'null'
```

stdout:

```
Schema validation errors were encountered.
```
