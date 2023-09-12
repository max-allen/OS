---
layout: page
title: Python's Import System
permalink: /python/import-system
---

# Python's Import System

Python files are run as scripts or modules.

Scripts are passed as an argument to the CLI directly:
```py
python myscript.py
```

Modules are imported by scripts or an interactive instance of the
interpreter:

```py
import fibo
```

The value of `__name__` is `__main__` when the file is loaded as script; as a
module it takes on the filename preceded by any packages or subpackages it
belongs to:

```py
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
    moduleA.py
```

Loading `moduleX` via import would result `__name__` having the value
`package.subpackage1.moduleX.py`.

## Relative Imports

The value of `__name__` is important because its what the interpreter will use
to resolve relative imports. Scripts can't perform relative imports because
`__name__` has a value of `__main__`:

```py
from .bar import foo
```

The above would result in an error, but that can be fixed by loading the file as module via the `-m` option:

```py
python -m package.bar.foo
```

#### References 📚
- [Relative Imports SO](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time)
- [Python Tutorial Module Section](https://docs.python.org/3/tutorial/modules.html)
