# ajv errors

```json
[
  {
    "instancePath": "",
    "keyword": "additionalProperties",
    "message": "must NOT have additional properties",
    "params": {
      "additionalProperty": "12"
    },
    "schemaPath": "#/anyOf/0/additionalProperties"
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
Traceback (most recent call last):
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/check_jsonschema/__main__.py", line 3, in <module>
    main()
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/check_jsonschema/__init__.py", line 26, in main
    ret = checker.run()
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/check_jsonschema/checker.py", line 88, in run
    self._run()
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/check_jsonschema/checker.py", line 71, in _run
    errors = self._build_error_map()
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/check_jsonschema/checker.py", line 63, in _build_error_map
    for err in validator.iter_errors(doc):
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/jsonschema/validators.py", line 229, in iter_errors
    for error in errors:
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/jsonschema/_validators.py", line 368, in anyOf
    errs = list(validator.descend(instance, subschema, schema_path=index))
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/jsonschema/validators.py", line 245, in descend
    for error in self.evolve(schema=schema).iter_errors(instance):
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/jsonschema/validators.py", line 229, in iter_errors
    for error in errors:
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/jsonschema/_validators.py", line 42, in additionalProperties
    extras = set(find_additional_properties(instance, schema))
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/site-packages/jsonschema/_utils.py", line 101, in find_additional_properties
    if patterns and re.search(patterns, property):
  File "/Users/ssbarnea/.pyenv/versions/3.10.3/lib/python3.10/re.py", line 200, in search
    return _compile(pattern, flags).search(string)
TypeError: expected string or bytes-like object
```
