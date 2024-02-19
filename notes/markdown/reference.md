---
layout: page
title: Markdown Reference
permalink: /markdown/reference/
---

# Markdown Reference

**Contents**
- [Headings](#headings)
- [Emphasis](#emphasis)
- [Lists](#lists)
- [Links](#links)
- [Images](#images)
- [Code](#code)
- [Blockquotes](#blockquotes)
- [Horizontal Rule](#horizontal-rule)

### Headings

```markdown
# h1
## h2
### h3
#### h4
##### h5
###### h6
```

```markdown
Header 1
========
```

```markdown
Header 2
--------
```

### Emphasis

```markdown
*italic*
_italic_
```

```markdown
**bold**
__bold__
```

```markdown
***bold italic***
___bold italic___
```

```markdown
~~strikethrough~~
```

```markdown
`code`
```

### Lists

```markdown
* Item 1
  * Nested Item 1
* Item 2
```

```markdown
- Item 1
  - Nested Item 1
- Item 2
```

```markdown
￼ Checkbox off
￼ Checkbox on
```

```markdown
1. Item 1
2. Item 2
```

### Links

```markdown
[link](http://google.com)
```

```markdown
[link][google]
[google]: http://google.com
```

```markdown
<http://google.com>
```

### Images

```markdown
![Image alt text](/path/to/img.jpg)
![Image alt text](/path/to/img.jpg "title")
```

```markdown
![Image alt text][img]
[img]: http://foo.com/img.jpg
```

### Code

```markdown
`inline code`
```

```
    4 space indent
    makes a code block
```

~~~markdown
```
code fences
```
~~~


~~~markdown
```js
codeFences.withLanguage()
```
~~~

### Blockquotes

```markdown
> This is
> a blockquote
>
> > Nested
> > Blockquote
```

### Horizontal Rule

```markdown
----
```

```markdown
****
```

### Tables

```markdown
| Column 1 Heading | Column 2 Heading |
| ---------------- | ---------------- |
| Some content     | Other content    |
```

```markdown
Column 1 Heading | Column 2 Heading
--- | ---
Some content | Other content
```

### References 📚