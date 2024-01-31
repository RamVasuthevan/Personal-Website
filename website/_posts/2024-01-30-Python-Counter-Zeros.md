---
layout: post
title: "Python Counter Subtraction Leaves Zeros"
image: /assets/bitsbipsbricks/Remove-Audio-Jack/74lirquirtl01.png
permalink: bitsbipsbricks/Python-Counter-Zeros
---

In Python, a [Counter](https://docs.python.org/3/library/collections.html#counter-objects) is a dictionary subclass with the keys being the element and the values being the element's count. The counter is initialized by passing in iterable or mapping. See below from standard library documentation:

> ```python
> c = Counter()                           # a new, empty counter
> c = Counter('gallahad')                 # a new counter from an iterable
> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
> ```

Once the Counter is created, the values be set to zero or negative numbers:

> ```python
> c1 = Counter([1, 1, 2, 2, 2])
> c1[1] = 0  # c1: Counter({1: 0, 2: 3})
> 
> c2 = Counter([1, 1, 2, 2, 2])
> c2[1] = -1  # c2: Counter({2: 3, 1: -1})
> ```

When a Counter is subtracted from another Counter by using `-`, the values are not set to zero or negative numbers

> ```python
> c1 = Counter([0, 1, 1, 2, 2, 2])
> c2 = Counter([0, 2, 2, 2, 3, 3])
> 
> print(c1 - c2)  # Counter({1: 1})
> ```

But when you use counter.subtract(), you are left with keys which value zero:

> ```python
> c1 = Counter([0, 1, 1, 2, 2, 2])
> c1.subtract([0, 2, 2, 2, 3, 3])
> 
> print(c1)  # Counter({1: 2, 0: 0, 2: 0, 3: -2})
> ```

From the standard library:
> For in-place operations such as c[key] += 1, the value type need only support addition and subtraction. So fractions, floats, and decimals would work and negative values are supported. The same is also true for update() and subtract() which allow negative and zero values for both inputs and outputs.

Having negative values makes senses but having a zero value is not expect behaviour to me. A common use case is to use a Counter as a mutliset (a set that allow multiple version of an element), but if we remove an element through subtract then the length of the Counter ie the number of disinct elements will not be correct anymore.

> ```python
> a = Counter([1, 2, 2])
> a.subtract([2, 2])
> 
> print(a)  # Counter({2: 2, 1: 0})
> 
> b = Counter([1])
> 
> print(a == b)  # True
> print(len(a) == len(b))  # False
> ```

Note: In 3.10+ for equality, missing elements are treated as having zero counts.

When we a  Counter as a mutlisets and need to remove an elementm, we either need to also check for zero values:

> ```python
> a.subtract([val])
> 
> if a[val] == 0:
>     del a[val]
> ```


Or use encapsulate the values in a counter:

> ```python
> a = a - Counter([val])
> ```


The first seems unnecessarily complex in the second seems wasteful. I understand that we might not want to change the behavior of subtract to preserve backward compatibility, or preserve symmetry with the negative value case. 

There should be a Counter.remove(val) method with removes val from the Counter. If the value now zero, than the count should not exist. If the values doee not exist, then an error should be thrown.