---
layout: page
title: Python Wiki
permalink: /python/wiki
published: false
---

# Python Wiki

**Contents**
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Application Specific Packages](#application-specific-packages)
- [Documentation](#documentation)

## Installation

MacOS comes with python preinstalled, but you should steer clear of this build as it’s used by Apple and third party software.

Package managers like Homebrew and apt-get are options for installation. I recommend installing a version manager like [pyenv](https://github.com/pyenv/pyenv) first so you can install multiple versions and comfortably switch between them as needed.

## Dependencies

[pip](https://pip.pypa.io/en/stable/) is the default package installer for Python; it’s installed in tandem with Python, so no need to install it explicitly. It downloads and installs packages from the [PyPI](https://pypi.org/), the Python Package Index.

## Project Dependencies

Working within the context of an application requiring specific versions of
python and project dependencies requires activating a virtual environment.
See [Python Dependency Management](./dependency-management).

## Documentation

- [Tutorial](https://docs.python.org/3/tutorial/index.html): Recommended
  starting point. Introduces basic concepts and features.
- [Library Reference](https://docs.python.org/3/library/index.html): Details the
  standard library distributed with Python.
- [Language Reference](https://docs.python.org/3/reference/index.html): Details
syntax and core semantics of the language.

<!-- ### 🚧 TODO:

- Environment Variables
- Conventions -->
