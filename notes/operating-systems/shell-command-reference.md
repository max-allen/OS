---
layout: page
title: Shell Command Reference
permalink: /operating-systems/shell-command-reference/
---
# Shell Command Reference

**Contents**

<!-- toc -->

- [Documentation](#documentation)
- [Files](#files)
  * [Add](#add)
  * [Delete](#delete)
  * [Read](#read)
  * [Edit](#edit)
  * [Rename](#rename)
  * [Move](#move)
  * [Copy](#copy)
  * [Locate](#locate)
  * [Type](#type)
- [System](#system)
  * [Shutdown / Reboot](#shutdown--reboot)
- [Networking](#networking)
- [Processes](#processes)
- [Shell](#shell)

<!-- tocstop -->

## Documentation
```sh
# retrieve manual
$ man brew

# see commands / usage
$ brew help

# see commands via flag
$ brew --help

# entering command without args may yield something
$ brew
```

## Files

### Add

```sh
# adds dir project-bar
$ mkdir project-bar

# adds file to dir project-bar
$ touch project-bar/__init__.py

# adds .bashrc if it does not exist via redirection
# .bashrc added with result of echo command
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
```

### Delete
```sh
# removes text file foo
$ rm foo.txt

# removes folder /bar recursively (-r)
$ rm -r /bar

# removes folder /baz and force deletes write protected files
$ rm -rf /baz

# removes qux interactively with prompting
$ rm -i /qux

# removes folder and json files
$ rm -rf node_modules/ *.json
```

### Read
```sh
# reads .ssh/known_hosts
$ cat ~/.ssh/known_hosts
```

### Edit
```sh
# opens file with vim for editing
$ vim project-bar/README.md
```

### Rename
```sh
# renames bar to foo
$ mv /bar /foo
```
### Move
```sh
# moves font file from Downloads to Fonts dir
$ mv ~/Downloads/dank-mono.otf ~/Library/Fonts/dank-mono.otf

# moves up a level
$ mv bar/* .
```

### Copy
```sh
# copies text files to /tmp
$ cp *.txt /tmp

# copies files in /tmp to junk recursively
$ cp -R junk /tmp
```

### Locate
```sh
# locates file in PATH
$ which pylint

# starts search at current dir for directory name foo
$ find . -type d -name foo

# searches for files containing bar
$ find . -type -f -name bar

# searches filesystem for files with ruby extension .rb
$ sudo find / -regex ".*\rb"
$ find / -name ".rb"

```
> `which` can be useful when you have multiple versions of an executable and
> don't know which will be executed.

### Type
```sh
# checks file for type, is dir
$ file thermald.bundle thermald.bundle

# > usr/share/thermaId.bundle: directory

# checks dir for type, is executable
$ file $PYENV_ROOT/shims/python-config

# > shims/python-config: Bourne-Again shell script text executable, ASCII text
```

> I've found this useful when working in file systems that commingle
> binaries with directories or files with uncommon extensions. Text files
> containing secrets or unstructured config files are also examples.

## System
### Shutdown / Reboot

```sh
# shutdown and reboot immediately
$ sudo shutdown -r now

# shutdown in ten minutes
$ sudo shutdown +10

# shutdown at Tue Nov 21 13:25:00 2023
# reboot at 2311211325 `yymmddhhmm`
$ sudo shutdown -r 2311211325
```
> `shutdown` will return a pid. terminate the process to abort the scheduled shutdown.

```sh
# shutdown output

# > Shutdown at Tue Nov 21 13:25:00 2023.
# > shutdown: [pid 78449]

# terminating the shutdown
$ kill 12923
```

TODO:

## Networking
```sh
# retrieve ip address
# ipconfig -a, ipconfig
```

## Processes
```sh
# retrieve processes for all users including processes without terminals
$ ps aux
```

## Shell
