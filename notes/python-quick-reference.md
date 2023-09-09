---
layout: page
title: Python Quick Reference
permalink: /python/
---

# Python Quick Reference

- [Memory Management](#memory-management)
- [Standard Library](#standard-library)
  - [Inspect](#inspect)
- [Dependency Management](#dependency-management)
  - [Virtual Environments](#virtual-environments)

## Memory Management

Memory allocation abstracted away, performed internally by the interpreter on demand.

https://docs.python.org/3/c-api/memory.html?highlight=memory%20management

## Standard Library
  ### Inspect

  Utilities for investigating live objects.
  [Standard Library Documentation](https://docs.python.org/3/library/inspect.html)

## Dependency Management

  ### Virtual Environments

  Virtual environments are Python's solution for application specific
  dependencies.

  > A cooperatively isolated runtime environment that allows Python users and applications to install and upgrade Python distribution packages without interfering with the behaviour of other Python applications running on the same system.

  [glossary
  entry](https://docs.python.org/3/glossary.html#term-virtual-environment)

  virtual envs created via the
  [venv](https://docs.python.org/3/library/venv.html#module-venv) module

  searching for package location within and outside of virtual env via pip:
  <!-- $HOME/.local/share/virtualenvs/dst-algorithms-OjA0cdcc/lib/python3.10/site-packages -->

  <!-- $HOME/.pyenv/versions/3.10.10/lib/python3.10/site-packages -->

  #### References 📚
  - [Python Lib Doc](https://docs.python.org/3/library/venv.html#module-venv)
  - [Packaging User Guide](https://packaging.python.org/en/latest/)
