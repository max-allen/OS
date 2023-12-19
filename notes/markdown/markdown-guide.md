---
layout: page
title: Markdown Guide
permalink: /markdown/guide
published: false
---

# Markdown

|  |  |
| -------- | -------- |
| Initial Release | October 2014 |
| Creators | [John Gruber](https://en.wikipedia.org/wiki/John_Gruber), [Aaron Swartz](https://en.wikipedia.org/wiki/Aaron_Swartz) |
| Spec | [CommonMark](https://commonmark.org/)
Maintainers | [John MacFarlane](https://usesthis.com/interviews/john.macfarlane/), [Martin Woodward](http://www.woodwardweb.com/), [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)
| Repo(s) | [Reference Implementation (Node)](https://github.com/commonmark/commonmark.js)

**Markdown** is a [plain text](https://en.wikipedia.org/wiki/Plain_text) (i.e.
human readable) format for writing structured documents. It's the predominant
markup language for writing on the web with ubiquitous support among text
editing application.

It was created as a human readable alternative to HTML, which is accessible to
non technical audiences.

### Use Cases

- Writing / Blogging
- Documentation (e.g. project READMEs)

Spec compliant parsers convert the language to an AST and render the document as
a markup language natively supported by web browsers (i.e. HTML, XML, etc.).

### Limitations

Markdown isn't natively supported by browsers so it will always require processing.

### Installation

Markdown transpilation is supported natively by many text editors. CommonMark is
a Node project and can be installed with npm or yarn.

### Components

Markdown is transpiled from plain text to HTML. A transpiler will perform the
parsing and translation to HTML before the document is rendered by a browser.
