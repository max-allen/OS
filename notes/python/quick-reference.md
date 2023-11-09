---
layout: page
title: Python Quick Reference
permalink: /python/quick-reference
---

# Python Quick Reference

**Contents**
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Documentation](#documentation)

## Installation

Python can be installed via Homebrew. Instead of installing python directly,
install python with [pyenv](https://github.com/pyenv/pyenv) so can you install
multiple versions and comfortably switch between them as needed.

## Dependencies

[pip](https://pip.pypa.io/en/stable/) is the default package installer for
Python. It installs packages from the [PyPI](https://pypi.org/), the Python
Package Index. Packages published to the registry can be installed like so:

```pip install <package name>```

Without an active virtual environment, this will install the relevant binary to
`$HOME/.pyenv/shims`.

### App Specific Dependencies

Working within the context of an application requiring specific versions of
python and project dependencies requires activating a virtual environment.
See [Python Dependency Management](./dependency-management).

## Documentation

Python is well documented. Orienting yourself to these should help you find what
you're looking for faster:

- [Tutorial](https://docs.python.org/3/tutorial/index.html): Recommended
  starting point. Introduces basic concepts and features.
- [Library Reference](https://docs.python.org/3/library/index.html): Details the
  standard library distributed with Python.
- [Language Reference](https://docs.python.org/3/reference/index.html): Details
syntax and core semantics of the language.

### How to Navigate

- If you don't have a conceptual understanding of a topic (e.g. modules) and are
looking for an informal orientation, see the tutorial docs.

- If you need to reference an API, see the standard lib docs.

- If you're looking for deep dive on how a component of the language works (e.g.
  the import system), see the language reference.

### 🚧 TODO:

- Environment Variables
- Conventions
