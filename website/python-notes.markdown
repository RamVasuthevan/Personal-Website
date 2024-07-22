---
layout: page
title: Python Notes
---

I don't really know what I am going to do on this page. But I have some notes about the Python Standard Library that I want to save for my future self.

# .islower()

Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise.

Cased characters are those with the Unicode general category property being one of “Lu” (Letter, uppercase), “Ll” (Letter, lowercase), or “Lt” (Letter, titlecase). This means that the method checks for characters that are specifically recognized as letters in their uppercase, lowercase, or titlecase forms.

 [See docs: str.islower()](https://docs.python.org/3/library/stdtypes.html#str.islower)

```python
print('a'.islower())   # True
print('A'.islower())   # False
print('1'.islower())   # False
print('a1'.islower())  # True
print('á'.islower())   # True
print('Á'.islower())   # False
print('汉'.islower())  # False  # Chinese character, not cased
print('ß'.islower())   # True  # German sharp s, considered lowercase
```