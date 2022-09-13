# ajv errors

```json
[
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
    "instancePath": "/galaxy_info",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "min_ansible_version"
    },
    "schemaPath": "#/additionalProperties"
  },
  {
    "instancePath": "/galaxy_info",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "galaxy_tags"
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

stdout:

```json
{
  "status": "fail",
  "errors": [
    {
      "filename": "negative_test/roles/meta/main.yml",
      "path": "$",
      "message": "{'galaxy_info': {'description': 'bar', 'min_ansible_version': '2.9', 'company': 'foo', 'license': 'MIT', 'galaxy_tags': 'database', 'platforms': [{'name': 'Alpine', 'versions': ['all']}]}} is not valid under any of the given schemas",
      "has_sub_errors": true,
      "best_match": {
        "path": "$.galaxy_info",
        "message": "Additional properties are not allowed ('galaxy_tags', 'min_ansible_version' were unexpected)"
      },
      "sub_errors": [
        {
          "path": "$.galaxy_info.galaxy_tags",
          "message": "'database' is not of type 'array'"
        },
        {
          "path": "$.galaxy_info",
          "message": "Additional properties are not allowed ('galaxy_tags', 'min_ansible_version' were unexpected)"
        }
      ]
    }
  ],
  "parse_errors": []
}
```
