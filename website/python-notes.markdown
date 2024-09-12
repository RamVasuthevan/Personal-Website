---
layout: page
title: Python Notes
---

I don't really know what I am going to do on this page. But I have some notes about the Python standard library that I want to save for my future self.

## .islower() (and .isupper())

Return `True` if all cased characters in the string are lowercase and there is at least one cased character, `False` otherwise.

Cased characters are those with the Unicode general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase). This means that the method checks for characters that are specifically recognized as letters in their uppercase, lowercase, or titlecase forms.

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

See more:
- [Python Documentation: str.islower()](https://docs.python.org/3/library/stdtypes.html#str.islower)


## Dictionary Ordering

As of Python 3.6 in CPython and 3.7 in all implementations [&#x2197;](https://docs.python.org/3/library/stdtypes.html#dict:~:text=changed%20in%20version%203.7%3A%20dictionary%20order%20is%20guaranteed%20to%20be%20insertion%20order.%20this%20behavior%20was%20an%20implementation%20detail%20of%20cpython%20from%203.6.), dictionaries are iterated in the insertion order of keys.

```python
d = {}

d[1] = True
d[2] = True
d[3] = True

print(d)  # {1: True, 2: True, 3: True}

d[2] = False
print(d)  # {1: True, 2: False, 3: True}

del d[2]
d[2] = True
print(d)  # {1: True, 3: True, 2: True}
```

### OrderedDict

OrderedDict can be used if you want to explicitly state the importance of the order or if you want to use methods like [.move_to_end()](https://docs.python.org/3/library/collections.html#collections.OrderedDict.move_to_end) or [.popitem()](https://docs.python.org/3/library/collections.html#collections.OrderedDict.popitem).

See more:
- [Real Python: OrderedDict vs dict in Python: The Right Tool for the Job](https://realpython.com/python-ordereddict/)
- [Python Documentation: collections.OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict)
- [Python Documentation: dict](https://docs.python.org/3/library/stdtypes.html#dict)


## Default Value for max() (and min())

If `max()` is given an sequence, it will raise a  `ValueError`. As of Python 3.4, the `max()` function supports a `default` parameter, which is returned if the provided sequence is empty. 

This is helpful when dealing with sequences of unknown length that could be empty.

```python
print(max([], default=0))  # 0
```

See more:
- [Python Documentation: max()](https://docs.python.org/3/library/functions.html#max)


## Get Python Version

```python
import sys

print(sys.version)  # '3.9.6 (default, Jul 27 2021, 07:03:06) [GCC 8.3.0]'
```

See more:
- [Python Documentation: sys.version](https://docs.python.org/3/library/sys.html#sys.version)


## dict.get()

The `dict.get()` method is a safe way to retrieve values from a dictionary without raising a `KeyError` if the key doesn't exist.

```python
dict.get(key, default=None)
```

This method returns the value for `key` if `key` is in the dictionary, else `default`. If `default` is not given, it defaults to `None`, so that this method never raises a `KeyError`.

```python
d = {'a': 1, 'b': 2}

print(d.get('a'))      # 1
print(d.get('c'))      # None
print(d.get('c', 0))   # 0

# Contrast with direct key access:
print(d['a'])          # 1
# print(d['c'])        # Raises KeyError
```

Useful when you want to handle missing keys without using a try-except block.

See more:
- [Python Documentation: dict.get()](https://docs.python.org/3/library/stdtypes.html#dict.get)

## itertools.islice()

`itertools.islice()` returns an iterator with selected elements using sequence slicing.

```python
itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])
```

The step argument must be positive, as iterators can be infinite.

```python
print(list(itertools.islice(range(10), 2, 8, 2)))  # [2, 4, 6]
```

See more:
- [Python Documentation: itertools.islice()](https://docs.python.org/3/library/itertools.html#itertools.islice)

## Walrus Operator (:=)

The walrus operator (`:=`), introduced in Python 3.8, allows assignment in expressions.

```python
# Assume expensive_function() is costly to compute
if (result := expensive_function()) > 100:
    print(f"Result {result} is large")
else:
    print(f"Result {result} is small")
```

Parentheses are sometimes required around the assignment expression, depending on context:

```python
# Parentheses required here
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")

# Parentheses not required here
while chunk := file.read(8192):
    process(chunk)
```

See more:
- [PEP 572 -- Assignment Expressions](https://www.python.org/dev/peps/pep-0572/)

## Pinning Dependencies in Pipfile

### Latest Version

```toml
[packages]
requests = "*"
beautifulsoup4 = "*"
```

### Pin Specific Versions

```toml
[packages]
requests = "==2.25.1"
beautifulsoup4 = "4.12.3"
```

### Pin in GitHub Dependabot


```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "daily"
    ignore:
      - dependency-name: "requests"
      - dependency-name: "beautifulsoup4"
```

## Timsort Space Complexity

Timsort sort has space complexity of **O(N)**:

> Timsort can require a temp array containing as many as N//2 pointers,
  which means as many as 2*N extra bytes on 32-bit boxes. It can be
  expected to require a temp array this large when sorting random data; on
  data with significant structure, it may get away without using any extra
  heap memory. This appears to be the strongest argument against it, but
  compared to the size of an object, 2 temp bytes worst-case (also expected-
  case for random data) doesn't scare me much.

Source: [Python/cpython - Objects/listsort.txt](https://github.com/python/cpython/blob/main/Objects/listsort.txt#L17C2-L23C47)
