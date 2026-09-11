# Python Collections – List, Tuple, Set and Dictionary

This README contains the basic syntax and commonly used operations for:

* List
* Tuple
* Set
* Dictionary

---

# 1. List

A **list** is an ordered and changeable collection.

### Creating a List

```python
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
```

### Accessing Elements

```python
print(fruits[0])
print(fruits[-1])
```

### Slicing

```python
print(fruits[0:2])
print(fruits[:2])
print(fruits[1:])
```

### Change an Element

```python
fruits[1] = "orange"
```

### Add Elements

```python
fruits.append("grapes")          # Add at the end

fruits.insert(1, "pineapple")    # Add at specific position

fruits.extend(["kiwi", "melon"]) # Add multiple elements
```

### Remove Elements

```python
fruits.remove("apple")  # Remove specific value

fruits.pop()            # Remove last element

fruits.pop(1)           # Remove element using index

del fruits[0]           # Delete using index

fruits.clear()          # Remove all elements
```

### List Length

```python
print(len(fruits))
```

### Check Element

```python
if "apple" in fruits:
    print("Apple is present")
```

### Sorting

```python
numbers.sort()                  # Ascending

numbers.sort(reverse=True)      # Descending

numbers.reverse()               # Reverse the list
```

### Copy List

```python
new_list = fruits.copy()
```

### Find Index

```python
print(fruits.index("mango"))
```

### Count Elements

```python
print(fruits.count("apple"))
```

### Loop Through List

```python
for fruit in fruits:
    print(fruit)
```

### List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
```

---

# 2. Tuple

A **tuple** is an ordered and unchangeable collection.

### Creating a Tuple

```python
fruits = ("apple", "banana", "mango")
numbers = (10, 20, 30, 40)
```

### Single Element Tuple

A comma is required:

```python
x = (10,)
```

Without the comma:

```python
x = (10)      # This is an integer
```

### Accessing Elements

```python
print(fruits[0])
print(fruits[-1])
```

### Slicing

```python
print(fruits[0:2])
print(fruits[1:])
```

### Check Element

```python
if "apple" in fruits:
    print("Apple is present")
```

### Tuple Length

```python
print(len(fruits))
```

### Count

```python
print(fruits.count("apple"))
```

### Find Index

```python
print(fruits.index("mango"))
```

### Loop Through Tuple

```python
for fruit in fruits:
    print(fruit)
```

### Tuple Unpacking

```python
fruits = ("apple", "banana", "mango")

a, b, c = fruits

print(a)
print(b)
print(c)
```

### Convert Tuple to List

```python
fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)

fruits_list.append("orange")

print(fruits_list)
```

### Convert List to Tuple

```python
fruits = ["apple", "banana", "mango"]

fruits_tuple = tuple(fruits)

print(fruits_tuple)
```

---

# 3. Set

A **set** is an unordered collection that does not allow duplicate values.

### Creating a Set

```python
fruits = {"apple", "banana", "mango"}

numbers = {10, 20, 30, 40}
```

### Important

Duplicate values are automatically removed:

```python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

### Empty Set

```python
my_set = set()
```

Do not use:

```python
my_set = {}
```

because `{}` creates an empty dictionary.

### Add Element

```python
fruits.add("orange")
```

### Add Multiple Elements

```python
fruits.update(["grapes", "kiwi"])
```

### Remove Element

```python
fruits.remove("apple")
```

`remove()` gives an error if the element does not exist.

```python
fruits.discard("apple")
```

`discard()` does not give an error if the element does not exist.

### Remove Random Element

```python
fruits.pop()
```

### Clear Set

```python
fruits.clear()
```

### Check Element

```python
if "apple" in fruits:
    print("Apple is present")
```

### Set Length

```python
print(len(fruits))
```

### Loop Through Set

```python
for fruit in fruits:
    print(fruit)
```

---

# 4. Set Operations

### Union

Combines elements from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)
```

You can also use:

```python
result = a | b
```

### Intersection

Returns common elements.

```python
result = a.intersection(b)

print(result)
```

Or:

```python
result = a & b
```

### Difference

Returns elements present in the first set but not the second.

```python
result = a.difference(b)

print(result)
```

Or:

```python
result = a - b
```

### Symmetric Difference

Returns elements that are not common to both sets.

```python
result = a.symmetric_difference(b)

print(result)
```

Or:

```python
result = a ^ b
```

### Subset

Checks whether one set is inside another set.

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
```

### Superset

Checks whether a set contains another set.

```python
print(b.issuperset(a))
```

### Disjoint

Checks whether two sets have no common elements.

```python
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
```

---

# 5. Dictionary

A **dictionary** stores data as **key-value pairs**.

### Creating a Dictionary

```python
student = {
    "name": "Athmik",
    "age": 20,
    "course": "Engineering"
}
```

### Accessing Values

```python
print(student["name"])
print(student["age"])
```

### Using `get()`

```python
print(student.get("name"))
```

`get()` is safer when the key may not exist:

```python
print(student.get("marks"))
```

### Change Value

```python
student["age"] = 21
```

### Add New Key-Value Pair

```python
student["marks"] = 85
```

### Remove Using `pop()`

```python
student.pop("age")
```

### Remove Last Item

```python
student.popitem()
```

### Delete Using `del`

```python
del student["name"]
```

### Clear Dictionary

```python
student.clear()
```

### Dictionary Length

```python
print(len(student))
```

### Check Key

```python
if "name" in student:
    print("Name exists")
```

---

# 6. Dictionary Methods

### Get All Keys

```python
print(student.keys())
```

### Get All Values

```python
print(student.values())
```

### Get Key-Value Pairs

```python
print(student.items())
```

### Update Dictionary

```python
student.update({
    "age": 21,
    "marks": 90
})
```

### Copy Dictionary

```python
new_student = student.copy()
```

---

# 7. Loop Through Dictionary

### Loop Through Keys

```python
for key in student:
    print(key)
```

### Loop Through Values

```python
for value in student.values():
    print(value)
```

### Loop Through Key and Value

```python
for key, value in student.items():
    print(key, value)
```

---

# 8. Dictionary with Different Data Types

```python
student = {
    "name": "Athmik",
    "age": 20,
    "marks": [80, 85, 90],
    "address": {
        "city": "Udupi",
        "state": "Karnataka"
    }
}
```

Access nested data:

```python
print(student["marks"][0])

print(student["address"]["city"])
```

---

# 9. Dictionary Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = {x: x * x for x in numbers}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```



# 11. Syntax Reference

### List

```python
my_list = [1, 2, 3]

my_list.append(4)
my_list.remove(2)
my_list.pop()
my_list.insert(1, 10)
my_list.sort()
```

### Tuple

```python
my_tuple = (1, 2, 3)

my_tuple.count(2)
my_tuple.index(2)
```

### Set

```python
my_set = {1, 2, 3}

my_set.add(4)
my_set.remove(2)
my_set.union({4, 5})
my_set.intersection({2, 3})
```

### Dictionary

```python
my_dict = {
    "name": "Athmik",
    "age": 20
}

my_dict["name"]
my_dict["age"] = 21
my_dict["marks"] = 90

my_dict.keys()
my_dict.values()
my_dict.items()
```

---





