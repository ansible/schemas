# Developing Schemas

You are welcome to contribute to the schemas for Ansible, Zuul and Molecule!

## Extending the schemas

Changes to the schemas need to be made in `src/ansibleschemas/`. They are then
generated with `tox` in the directory `f/`. The generated files need to be
included with each commit as that's the way they are published at the moment.

### Updating the Galaxy Platforms

`GALAXY_PLATFORMS` in `src/ansibleschemas/_galaxy.py` lists the commonly known
platforms and versions available on Galaxy. They can be viewed visiting
https://galaxy.ansible.com/api/v1/platforms/.

For updating the list of platforms and versions you can set the environment variable
`DUMP_GALAXY_PLATFORMS` and run `tox`:

```shell
DUMP_GALAXY_PLATFORMS=1 tox
```

This will query the API and replace the current list of galaxy platforms.

### Updating dependencies

Run the following command to update dependency lock files `constraints.txt`
and `package-lock.json`:

```shell
tox -e deps
```

## Submitting Pull Requests

Fixes and features for schemas will go through the Github pull request process.
Submit your pull request (PR) against the `main` branch.

Here are a few things you can do to help get your pull request accepted faster:

- Check that the following commands run without reporting any errors
  - python tests: `tox`
  - validation tests using mocha: `npm test`
- Write good commit messages. See [How to write a Git commit message](https://chris.beams.io/posts/git-commit/).

## Reporting Issues

We welcome your feedback, and encourage you to file an issue when you run into
a problem.
