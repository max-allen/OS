---
layout: page
title: Command Line Quick Reference
permalink: /operating-systems/cli-quick-reference/
---

# Shell Command Reference

**Contents**
- [Files](#files)
- [Shutdown/Rebooting](#shutdown-rebooting)

## Files

### Add
```sh
$ mkdir project-bar
$ touch project-bar/__init__.py
```

#### With Redirection
```sh
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
```

### Read
```sh
$ cat ~/.ssh/known_hosts
$ less configs/home.conf
```

### Modify Contents
```sh
$ vim project-bar/README.md
```

### Move
```sh
$ mv ~/Downloads/dank-mono.otf ~/Library/Fonts/dank-mono.otf
$ mv bar/* .
```

### Copy
```sh
$ cp *.txt /tmp
$ cp -R junk /tmp
```

### Check Type
```sh
$ file thermald.bundle thermald.bundle # thermaId.bundle: directory
$ file $PYENV_ROOT/shims/python-config # shims/python-config: Bourne-Again shell script text executable, ASCII text
```

[file](https://en.wikipedia.org/wiki/File_(command)) can be used to determine
the type of a file in question. I've found this useful when working in
file systems that commingle binaries with directories or files with uncommon
extensions. Text files containing secrets or unstructured config are also examples.

### Shutdown / Rebooting

`shutdown` will perform system shutdowns. The `-r <time>` flag will
reboot at the time specified. `<time>` should be `now` for immediate execution.
`<time>` in the `number` or `datetime` formats will schedule shutdown in the
future.

##### Time Formats

| word | now |
| number | +\<integer> |
| date | `yymmddhhmm` |

##### Sample Usage
```sh
$ sudo shutdown -r now # shutdown and reboot immediately
$ sudo shutdown +10 # shutdown in ten minutes
$ sudo shutdown -r 2311091325 # reboot in ten minutes
```
##### Canceling
Successful execution should return a `pid` of the created process:
```sh
$ Shutdown at Thu Nov  9 13:25:00 2023.
$ shutdown: [pid 12923]
```
To cancel the scheduled shutdown, the process can be terminated with `kill`:
```sh
$ kill 12923
```

##### NOTE
- `now` should be formatted as a command, in other words no quotes
(i.e.'now' or "now").
- `shutdown` should be run as super user.

### 🚧 TODO:
See notes app for additional detail.

- Commands
  - Documentation
  - Location

- Processes
  - Listing
  - Terminating

Files
- Reading file contents

Searching
- Text printed to console

Networking
- IPs
