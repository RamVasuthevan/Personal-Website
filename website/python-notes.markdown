---
layout: page
title: Python Notes
---

I don't really know what I am going to do on this page. But I have some notes about the Python Standard Library that I want to save for my future self.

## .islower()

Return `True` if all cased characters in the string are lowercase and there is at least one cased character, `False` otherwise.

Cased characters are those with the Unicode general category property being one of “Lu” (Letter, uppercase), “Ll” (Letter, lowercase), or “Lt” (Letter, titlecase). This means that the method checks for characters that are specifically recognized as letters in their uppercase, lowercase, or titlecase forms.


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



## Default Value for max()

If `max()` is given an sequence, it will raise a  `ValueError`.  s of Python 3.4, the `max()` function supports a `default` parameter, which is returned if the provided sequence is empty. 

This is helpful when dealing with sequences of unknown length that could be empty.

### Example

```python
print(max([], default=0))  # 0
```

See more:
- [Python Documentation: max()](https://docs.python.org/3/library/functions.html#max)
