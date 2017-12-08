# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples don't change - they are immutable.  Lists can be changed.  They can grow, shrink, etc.

Tuples and lists are similar because they have the same format - they look the same.

Tuples can be used as keys in dictionaries because they are hashable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are similar in the sense that they're collections of items.  But lists have a guaranteed order and can have multiple elements with the same value.  In that sense, a list's focus is a position, a slot and what's in that slot.  A set's focus is on the value, not the slot, and whether the value is in the SET, not a position in an ordered list.

Since a set's entire purpose is what's "IN" the set, it's set up internally as a hash.  A set must be able to determine whether a "new" element is already in the set when tries to add it.  A list doesn't - it just tacks it at the end.  So the machinery for "finding an element" is already baked into the very structure underyling the functionality of a set.  


---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

A lambda is sort of a one-line function.  In python it's often directly interchangeable with a function definition.

```python
def this_is_a_function(x,y)
	return x+y

lambda x,y: x+y

```

The sorted function uses a hash function of a kind to map from whatever's being sorted into the thing that's actually geing compared for sorting.  This has replaced the now deprecated "cmp" argument which was doing a similar thing but in a more verbose, repetitive fashion.

```python
sorted(list_of_lists,key=lambda x:x[1])

```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions flip around iteration to avoid the necessity of writing out the loop syntax.

These are equivalent:

```python
a1 = range(10)
a2 = list()
for a in a1:
	a2.append(1+a)
```

```python
a1 = range(10)
a2 = [x+1 for x in a1]
```

Equivalence of using map with list and a list comprehension:

```python
a1 = range(10)
a2 = list(map(lambda x: x+1, a1)) # list needed because Python 3 is lazy here
```


```python
a1 = range(10)
a2 = [(lambda x:x+1)(a) for a in a1] # including lambda here to show equivalence - could have been a function call
```

Equivalence of using filter with list and a list comprehension:

```python
a1 = range(10)
a2 = list(filter(lambda x:x>5,a1))
```

```python
a1 = range(10)
a2 = [a for a in a1 if x>5] # dropping the lambda this time, because...
```

Dictionary comprehension:

```python
a1 = range(10)
a2 = {a:a+1 for a in a1]}
```

Set comprehension:
```python
{ x%4 for x in range(20)}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





