# Writing Tests

Unit Testing

Testing individual units in isolation (e.g. inputs, outputs).

In practice there's commonly variation in scope: could be testing an individual function, or a set of related packages/modules. In my experience describing something as a unit test is more indicative of test style than scope under test.

Rules of Thumb

- If a method or class only exists to support one or two other classes (e.g. helper), it should probably be tested within the testing suite for the functionality it supports instead of tested directly.

Benefits

Because scope is small, they're relatively easy to write.

They make it easy to understand what's wrong given failure because they minimize scope.

Can serve as documentation or example usage for how a part of the system should be used

Tests should prioritize maintainability. You should be able to write it once, then forget about it until it fails. Test failures should indicate real bugs with clear causes.

Maintainability

Minimize brittle tests. Tests should never change given a harmless or unrelated change _that doesn't introduce bugs_. Test failures should always be clear.

Anti-Brittle Strategies

**Author Tests That Won't Change**

- exceptions are changes in requirements

**Test with Public APIs**

_Test the system the same way users will._

- improves reliability of failures: a change that breaks a test should affect user

- API private method example: Public API with private methods. By leveraging its internal state during testing, it interacts with the API differently than users would. Tests exposed to refactor / change of internals

- It's not uncommon to encounter resistance testing in this fashion – it's easier to write tests limited to the marginal change you've authored, as opposed to considering how that change affects the broader system

https://testing.googleblog.com/2015/01/testing-on-toilet-prefer-testing-public.html

**Test State, Not Interactions**
