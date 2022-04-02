# Schemas for Ansible and its related tools

[![ci](https://github.com/ansible-community/schemas/actions/workflows/npm.yml/badge.svg)](https://github.com/ansible-community/schemas/actions/workflows/npm.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Repository License: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

## About Schemas

This project aims to generate JSON/YAML validation schemas for Ansible files
such as playbooks, tasks, requirements, meta or vars and also for Molecule
configuration.

Keep in mind that these schemas will limit your freedom of choice regarding the
syntax you can use to write Ansible tasks as they do not allow some historical
forms which are still allowed by Ansible itself.

Not any file accepted by Ansible will pass these schemas but we do expect that
any file that passed these schemas should be accepted by Ansible.

- YAML 1.2 booleans are required as `true` or `false`, while Ansible itself
  allows you to use more relaxed forms like `yes` or `no`.
- Inline actions are not allowed, as schema cannot validate them
- Non builtin modules must be called using `action:` blocks
- Module arguments are not yet verified but we plan to implement it

As these schemas are still experimental, creating pull-requests to improve the
schema is of much greater help. Though you are still welcome to report bugs but
expect them to take a longer time until someone finds time to fix them.

If you want to help improve the schemas, have a look at the
[development documentation](CONTRIBUTING.md).

## Schema Bundle

We are currently migrating towards a single [ansible.json](/f/ansible.json)
schema bundle, one that contains subschema definitions for all the supported
file types.

To configure your validator or editor to use the bundle, use the new URLs below,
the part after the `#` in the URLs is essential for informing the loader about
which subschema to use. You can also look at our own
[settings.json](.vscode/settings.json) to understand how to configure
[vscode-yaml](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
extension.

- [playbook subschema url](https://raw.githubusercontent.com/ansible/schemas/main/f/ansible.json#/definitions/playbook)
- [tasks subschema uri](https://raw.githubusercontent.com/ansible/schemas/main/f/ansible.json#/definitions/tasks)

## Activating the schemas

At this moment installing
[Ansible VS Code Extension by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
will activate these schemas. The file patterns used to trigger their use can be
seen
[here](https://github.com/ansible-community/vscode-ansible/blob/master/package.json#L44-L94)

Because these schemas are generic, you can easily use them with any validators
that support them.
