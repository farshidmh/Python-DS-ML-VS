# Lab: Python Conditionals

## Objective

Learn the fundamentals of conditional statements in Python, including how to use `if`, `elif`, and `else` blocks. Discover Python's approach to logical operations, which is distinct from many other
programming languages due to its readability and simplicity. By the end of this lab, you should be able to write Python code that makes decisions based on conditions.

## Time to Complete

30 minutes

## Introduction

Python differs from many other programming languages:

- It uses indentation to define code blocks, instead of curly braces.
- Logical operators are written as `and` and `or`, not `&&` and `||`.
- Python's syntax aims to be more readable and expressive.

## Instructions

### Before You Begin

Ensure your Python environment is set up and ready for coding. You can use a text editor with a Python interpreter or a Jupyter Notebook.

### Basic Conditional Statements

- **Task 1**: Write a Python script that declares a variable `a` with a value of `2`. Use `if`, `elif`, and `else` statements to print:
    - "less than one" if `a` is less than `1`
    - "between one and two" if `a` is between `1` and `2`
    - "greater than 2" otherwise

```python
a = 2

if a < 1:
    print("less than one")
elif 1 <= a < 2:
    print("between one and two")
else:
    print("greater than 2")
```

### Simplifying Conditions

You can simplify conditions in Python, making your code cleaner and more readable.

- **Task 2**: Use Python's ability to chain comparison operators to simplify complex logical conditions.

```python
a = 1
if a < 1:
    print("less than one")
elif 1 <= a < 2:
    print("between one and two")
else:
    print("greater than 2")
```

### Logical NOT

Explore how to invert conditions using `not`.

- **Task 3**: Write a condition using `not` to invert a comparison.

```python
a = 10
b = 20

if not a > b:
    print('a is NOT greater than b')
```

### Exercise: Finding the Largest Value

Write code that compares three variables (`x`, `y`, `z`) and prints which one is the largest.

```python
x = 2
y = 3
z = 4

if x > y and x > z:
    print("x")
elif y > x and y > z:
    print("y")
else:
    print("z")
```

### One-liners

Python supports one-liner conditional assignments, providing a concise way to assign values based on conditions.

- **Task 4**: Use a one-liner to assign the greater of two variables `a` and `b` to a new variable `max`.

```python
a = 10
b = 15
max = a if (a > b) else b
print(max)
```

### String Comparisons

Comparing strings in Python is straightforward and intuitive.

- **Task 5**: Compare two strings for equality and print "Correct" if they match, or "Incorrect" otherwise.

```python
correct_password = "spam"
password = "ham"

if correct_password == password:
    print("Correct")
else:
    print("Incorrect")
```

### Checking for Null/Empty Values

Understand how Python treats null/empty values in conditions.

- **Task 6**: Experiment with different values (including `None`, empty strings, `True`, `False`, etc.) to see how they evaluate in a conditional statement.

```python
a = None  # Try different values here

if a:
    print("not null")
else:
    print("null")
```

### Exercise: Simple Password Checker

Create a simple password checker with specific criteria.

```python
password = 'example'

if len(password) < 5:
    print('too short')
elif len(password) > 20:
    print('too long')
elif '!' not in password:
    print('need an exclamation')
elif 'password' in password.lower():
    print('try another one')
else:
    print('password is okay')
```

### Conclusion

You've learned how to use Python's conditional statements to make decisions based on conditions. Practice writing more complex conditions and using these concepts in real-world scenarios to solidify
your understanding.