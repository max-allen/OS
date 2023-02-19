# Code Change Types

**Pure Refactorings**

- this is a refactor that modifies the internals of a system without changing the behavior of the system or interface
- tests should ensure the refactoring hasn't resulted in change of a system's behavior
- if tests need to be changed, this indicates the refactor isn't pure (something has affected the systems behavior), or tests weren't written at an appropriate level of abstraction

**New Features**

- Addition of new features. Behavior should be covered. Changes to existing tests indicate a possible regression or inappropriate tests

**Bug Fixes**

- Should be viewed similarly to new features. Presence of a bug indicates missing case from test suite, and fix should accompany new test case

**Behavior Changes**

- These changes break an explicit contract of the system. They are expensive. Tests will need to be updated (or replaced), and users of the system will likely be affected.

> This is the only category of change where change should be expected