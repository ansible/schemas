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
    "instancePath": "/dependencies/0",
    "keyword": "required",
    "message": "must have required property 'role'",
    "params": {
      "missingProperty": "role"
    },
    "schemaPath": "#/definitions/DependencyModel/anyOf/0/required"
  },
  {
    "instancePath": "/dependencies/0",
    "keyword": "required",
    "message": "must have required property 'src'",
    "params": {
      "missingProperty": "src"
    },
    "schemaPath": "#/definitions/DependencyModel/anyOf/1/required"
  },
  {
    "instancePath": "/dependencies/0",
    "keyword": "required",
    "message": "must have required property 'name'",
    "params": {
      "missingProperty": "name"
    },
    "schemaPath": "#/definitions/DependencyModel/anyOf/2/required"
  },
  {
    "instancePath": "/dependencies/0",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/definitions/DependencyModel/anyOf"
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
  negative_test/roles/role_with_bad_deps_in_meta/meta/main.yml::$: {'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}, 'dependencies': [{'version': 'foo'}]} is not valid under any of the given schemas
  Underlying errors caused this.
  Best Match:
    $: {'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}, 'dependencies': [{'version': 'foo'}]} is not of type 'null'
```

stdout:

```
Schema validation errors were encountered.
```
