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
    "instancePath": "/galaxy_info/author",
    "keyword": "pattern",
    "message": "must match pattern \"^[a-z\\d](?:[a-z\\d]|-(?=[a-z\\d])){0,38}$\"",
    "params": {
      "pattern": "^[a-z\\d](?:[a-z\\d]|-(?=[a-z\\d])){0,38}$"
    },
    "schemaPath": "#/properties/author/pattern"
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

stdout:

```json
{
  "status": "fail",
  "errors": [
    {
      "filename": "negative_test/roles/v1_meta_author/meta/main.yml",
      "path": "$",
      "message": "{'galaxy_info': {'author': 'foo.bar', 'description': 'foo', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$",
        "message": "{'galaxy_info': {'author': 'foo.bar', 'description': 'foo', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not of type 'null'"
      },
      "sub_errors": [
        {
          "path": "$",
          "message": "{'galaxy_info': {'author': 'foo.bar', 'description': 'foo', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not of type 'null'"
        },
        {
          "path": "$.galaxy_info.author",
          "message": "'foo.bar' does not match '^[a-z\\\\d](?:[a-z\\\\d]|-(?=[a-z\\\\d])){0,38}$'"
        }
      ]
    }
  ],
  "parse_errors": []
}
```
