# Developing Schemas

You are welcome to contribute to the schemas for Ansible and Molecule!

## Setting up the project for development

You need node.js version 16 or newer.

To set up the project, go to the project root directory and run:

```shell
npm install
```

## Extending the schemas

The schemas are in the directory `f/`. You can modify them directly.

### Updating dependencies

To update the dependency lock file `package-lock.json`, go to the project root
directory and run:

```shell
npm run deps
```

## Submitting Pull Requests

Fixes and features for schemas will go through the Github pull request process.
Submit your pull request (PR) against the `main` branch.

Here are a few things you can do to help get your pull request accepted faster:

- Run `npm test` and check that it returns without reporting any errors.
- Write good commit messages. See
  [How to write a Git commit message](https://chris.beams.io/posts/git-commit/).

## Reporting Issues

We welcome your feedback and encourage you to file an issue when you run into a
problem.
