# ajv errors

```json
  {
    instancePath: '',
    schemaPath: '#/anyOf/0/type',
    keyword: 'type',
    params: { type: 'null' },
    message: 'must be null'
  },
  {
    instancePath: '/galaxy_info/namespace',
    schemaPath: '#/properties/namespace/pattern',
    keyword: 'pattern',
    params: { pattern: '^[a-z][a-z0-9_]+$' },
    message: 'must match pattern "^[a-z][a-z0-9_]+$"'
  },
  {
    instancePath: '',
    schemaPath: '#/anyOf',
    keyword: 'anyOf',
    params: {},
    message: 'must match a schema in anyOf'
  }
]
```


# check-jsonschema

stdout:

```json
{
  "status": "fail",
  "errors": [
    {
      "filename": "negative_test/roles/meta_invalid_role_namespace/meta/main.yml",
      "path": "$",
      "message": "{'galaxy_info': {'description': 'foo', 'min_ansible_version': '2.9', 'namespace': 'foo-bar', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not>
      "has_sub_errors": true,
      "best_match": {
        "path": "$",
        "message": "{'galaxy_info': {'description': 'foo', 'min_ansible_version': '2.9', 'namespace': 'foo-bar', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is n>
      }
    }
  ]
}
```
