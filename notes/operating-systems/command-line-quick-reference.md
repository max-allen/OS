---
layout: page
title: Command Line Quick Reference
permalink: /operating-systems/cli-quick-reference/
---

# Command Line Quick Reference

**Contents**
- [Shutdown/Rebooting](#shutdown-rebooting)

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
```bash
sudo shutdown -r now # shutdown and reboot immediately
sudo shutdown +10 # shutdown in ten minutes
sudo shutdown -r 2311091325 # reboot in ten minutes
```
##### Canceling
Successful execution should return a `pid` of the created process:
```bash
Shutdown at Thu Nov  9 13:25:00 2023.
shutdown: [pid 12923]
```
To cancel the scheduled shutdown, the process can be terminated with `kill`:
```bash
kill 12923
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

- Files
  - Adding / removing
  - Moving
  - Copying
  - Reading contents

- Processes
  - Listing
  - Terminating

Files
- Reading file contents

Searching
- Text printed to console

Networking
- IPs
