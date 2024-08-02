# Lab: Exploring Python Data Structures

## Objective

This lab introduces you to Python's fundamental data structures: tuples, lists, sets, and dictionaries. You will learn their characteristics, how to create and manipulate them, and their use-cases in
programming. By the end of this lab, you should be comfortable working with these data structures for data storage and manipulation in Python.

## Time to Complete

45 minutes

## Instructions

### Before You Begin

Ensure you have a Python environment ready where you can execute Python code, such as Jupyter Notebook, PyCharm, VSCode, or any other IDE of your choice.

### 1. Tuples

Tuples are immutable sequences, which means once a tuple is created, its content cannot be changed.

- **Task 1.1**: Create a tuple containing items of different data types, print the tuple, and its type.

```python
t = (1, 3.14, 'hi')
print(t)
print(type(t))
```

- **Task 1.2**: Access the first and third items in the tuple using indexing.

```python
print(t[0])  # Accessing the first item
print(t[2])  # Accessing the third item
```

- **Task 1.3**: Attempt to modify the first item in the tuple to observe the immutability property.

```python
# This should raise an error
t[0] = 2
```

### 2. Lists

Lists are ordered, mutable sequences, allowing duplicate elements.

- **Task 2.1**: Create a list containing various data types, including duplicates. Print the list.

```python
mylist = ['abc', 10, 20.5, 10]
print(mylist)
```

- **Task 2.2**: Access the first item and the items from the second to the last. Print the results.

```python
print(mylist[0])   # Accessing the first item
print(mylist[1:])  # Accessing items from the second to the last
```

- **Task 2.3**: Change the second item in the list to a new value. Print the modified list.

```python
mylist[1] = 100
print(mylist)
```

### 3. Sets

Sets are unordered collections of unique elements.

- **Task 3.1**: Create a set with duplicates and print it to observe the automatic removal of duplicates.

```python
s1 = set([1, 2.2, "a", "b", "c", "a"])
print(s1)
```

- **Task 3.2**: Add a new element to the set and print the set.

```python
s1.add('d')
print(s1)
```

### 4. Dictionaries

Dictionaries store key-value pairs, allowing quick value retrieval using keys.

- **Task 4.1**: Create an empty dictionary, add some key-value pairs, and print it.

```python
d1 = {}
d1['one'] = 1
d1['two'] = 2
print(d1)
```

- **Task 4.2**: Create a dictionary with personal information (name, address, city, age) and print it.

```python
d2 = {'name': 'Tim', 'address': '123 Main Street', 'city': 'Seattle', 'age': 20}
print(d2)
```

- **Task 4.3**: Print only the keys and then only the values of the dictionary.

```python
print(d2.keys())
print(d2.values())
```

- **Task 4.4**: Create a nested dictionary representing an address, and pretty print it using the `pprint` module.

```python
import pprint
d3 = {'name': 'Tim', 'address': {'street': '123 Main Street', 'city': 'Seattle', 'state': 'Washington'}}
pprint.pprint(d3, indent=4)
```

### 5. Getting Default Values from Dictionaries

Learn to handle missing keys in dictionaries gracefully using the `get` method.

- **Task 5.1**: Demonstrate the use of the `get` method to retrieve a value with a default for missing keys.

```python
d = {'name': 'Tim'}
print("name:", d.get('name', 'Unknown'))
print("age:", d.get('age', 'Unknown'))
```

### Practice

Now, it's your turn to create and manipulate your data structures. Experiment with tuples, lists, sets, and dictionaries. Try adding, removing elements, and accessing elements in different ways.

### Exercise 1: Personal Record

Create a personal record using all the data structures learned. Use the template provided in the instructions to include your name, age, height, address, phones, email, and social media handles in the
appropriate data structures.

```python
# Creating a personal record using Python data structures

# Personal Information
person = {}
person['name'] = 'John Doe'  # String
person['age'] = 30  # Integer
person['height'] = 5.9  # Float

# Address Information
person['address'] = {
    'street': "123 Main St",
    'city': "Seattle",
    'state': "WA"
}  # Dictionary

# Phone Numbers
person['phones'] = ['123-456-7890', '098-765-4321']  # List (duplicates allowed)

# Email Addresses
person['email'] = {'john@example.com', 'doe@example.com'}  # Set (no duplicates allowed)

# Social Media Handles
person['social'] = {
    'twitter': '@johndoe',
    'facebook': 'fb.com/johndoe'
}  # Dictionary (no duplicate keys allowed)

# Displaying the structured personal record
import pprint
pprint.pprint(person, indent=2)
```