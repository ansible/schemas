"""Utility to generate some complex patterns."""
import keyword
import json

play_keywords = list(filter(None, """\
any_errors_fatal
become
become_exe
become_flags
become_method
become_user
check_mode
collections
connection
debugger
diff
environment
fact_path
force_handlers
gather_facts
gather_subset
gather_timeout
handlers
hosts
ignore_errors
ignore_unreachable
max_fail_percentage
module_defaults
name
no_log
order
port
post_tasks
pre_tasks
remote_user
roles
run_once
serial
strategy
tags
tasks
throttle
timeout
vars
vars_files
vars_prompt
""".split()))


invalid_var_names = sorted(list(keyword.kwlist) + play_keywords)
print("Updating invalid var names")

with open("f/ansible-vars.json", "r+", encoding="utf-8") as f:
    vars_schema = json.load(f)
    vars_schema['anyOf'][0]['patternProperties'] = {
        f"^(?!{'|'.join(invalid_var_names)})[a-zA-Z_][\\w]*$": {}
    }
    f.seek(0)
    json.dump(vars_schema, f, indent=2)
    f.write("\n")
    f.truncate()
