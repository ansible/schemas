# Schemas for Ansible and Zuul

This project that aims to generate JSON/YAML validation schemas for Ansible
files as playbooks, tasks, requirements, meta or vars.

Keep in mind that these schemas will limit your freedom of choice regarding
the syntax you can use to write Ansible tasks as they do not allow some
historical forms which are still allowed by Ansible itself.

Not any file accepted by Ansible will pass these schemas but we do expect
that any file that passed these schemas should be accepted by Ansible.

* YAML 1.2 booleans are required as `true` or `false`, while Ansible itself
  allows you to use more relaxed forms like `yes` or `no`.
* Inline actions are not allowed, as schema cannot validate them
* Non builtin modules must be called using `action:` blocks
* Module arguments are not yet verified but we plan to implement it

As these schemas are experimental, please refrain from reporting bugs but
feel free to create pull-requests to improve the schema.

## Activating the schemas

At this moment installing [Ansible Language for vscode extension](https://marketplace.visualstudio.com/items?itemName=zbr.vscode-ansible)
will activate these schemas. The file patterns used to trigger their use can be
seen [here](https://github.com/ansible-community/vscode-ansible/blob/master/package.json#L86)

Because these schemas are generic, you can easily use them with any validators
that support them.
