---
layout: page
title: Filesystem Hierarchy Reference
permalink: operating-systems/filesystem-hierarchy/reference/
---
# Filesystem Hierarchy Reference

Reference for the directory structure of Unix-like systems. These conventions
are popular among Linux distributions and established by the [Filesystem
Hierarchy Standard](https://wiki.linuxfoundation.org/lsb/fhs) maintained by the
Linux Foundation.

- [Usage](#usage)
- [Reference](#reference)
- [Resources](#resources-%F0%9F%93%9A)

### Usage

- **How:** Use to assist recall of file structure on Unix like systems.
- **When:** Managing prod infra. Investigating processes running on a host.

### Reference

| **Directory** | **Description** |
| -------- | -------- |
| `/` | root directory of filesystem |
| `/bin` | essential binaries |
| `/boot` | kernel boot loader files  |
| `/dev` | interfaces to device drivers |
| `/etc` | system configuration files |
| `/home` | personal directories for users |
| `/lib` | library files for binaries in `/bin`, `/sbin` |
| `/media` | attachment point for removable media (e.g. external hard drive) |
| `/mnt` | temporarily mounted filesystems |
| `/opt` | optional application software packages |
| `/proc` | virtual filesystem providing process and kernel info as files |
| `/root` | root users home directory |
| `/run` | information about running system since last boot |
| `/sbin` | essential system binaries |
| `/srv` | site specific data served by the system |
| `/tmp` | storage for temporary files |
| `/usr` | user installed software |
| `/var` | variable files subject to change (logs, caches, user tracking) |

### Resources 📚
- [Linux Journey](https://linuxjourney.com/lesson/filesystem-hierarchy)
- [Filesystem Hierarchy Standard Wiki](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard#cite_note-1)
