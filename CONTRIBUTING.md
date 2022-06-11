# Developing Schemas

You are welcome to contribute to the schemas for Ansible and Molecule!

## Setting up the project for development

We are using `task`[https://taskfile.dev/] as a build tool and if you want to
see the list of tasks available without running them run `task -l` or look
inside `Taskfile.yml`.

## Extending the schemas

The schemas are in the directory `f/`. You can modify them directly.

### Updating dependencies

To update the test dependencies run `task deps` and if all tests are passing
make a pull request to update them.

## Submitting Pull Requests

Fixes and features for schemas will go through the Github pull request process.
Submit your pull request (PR) against the `main` branch.

Here are a few things you can do to help get your pull request accepted faster:

- Run `task` and check that it returns without reporting any errors.
- Write good commit messages. See
  [How to write a Git commit message](https://chris.beams.io/posts/git-commit/).

## Reporting Issues

We welcome your feedback and encourage you to file an issue when you run into a
problem.
