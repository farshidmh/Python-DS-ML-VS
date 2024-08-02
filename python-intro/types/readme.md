# Lab: Introduction to Python Programming

## Objective
In this lab, you'll practice the fundamentals of Python programming, including working with different data types, declaring variables, manipulating strings, and converting between types. This hands-on experience will help you become familiar with Python syntax and basic programming concepts.

## Lab Overview
This lab is divided into several sections, each designed to introduce you to key aspects of Python programming. You'll start with basic concepts and progressively move on to more complex operations, particularly focusing on strings and type conversion.

### Before You Begin
Make sure you have access to a Python environment where you can write and execute code. This could be a Jupyter Notebook, an IDE like PyCharm or VSCode, or a simple text editor with a command-line interface.

## Time to Complete

This lab should take approximately **30 minutes** to complete.

## Instructions

### 1. Python Types
Python is a dynamically typed language, meaning you don't have to declare the type of a variable explicitly. This feature is known as "duck typing."

- **Task 1.1**: In your Python environment, create variables of different types (integer, float, string) and use the `print` statement and `type()` function to display their types.

```python
# Task 1.1 Code Snippet
a = 10  # Integer
b = 5.5  # Float
c = "Hello, World!"  # String

print(type(a))
print(type(b))
print(type(c))
```

### 2. Declaring Variables
Unlike statically typed languages, Python allows you to declare variables without specifying their types, making the code cleaner and more readable.

- **Task 2.1**: Declare an integer variable, a floating-point variable, and a string variable. Then, print their values.

```python
# Task 2.1 Code Snippet
my_int = 42
my_float = 3.14159
my_string = "Python is fun!"

print(my_int)
print(my_float)
print(my_string)
```

### 3. Working with Strings
Strings in Python can be enclosed in either single quotes (`'`) or double quotes (`"`), and you can manipulate them in various ways.

#### 3.1 Defining Strings
- **Task 3.1**: Create two variables containing string values, using both single and double quotes. Access and print the first three characters of each string.

```python
# Task 3.1 Code Snippet
string1 = 'Hello'
string2 = "World"

print(string1[:3])
print(string2[:3])
```

#### 3.2 Joining Strings
- **Task 3.2**: Concatenate (join) two strings together, and print the result. Then, modify your code to include a space between the two strings and print the result again.

```python
# Task 3.2 Code Snippet
s1 = "Hello"
s2 = "World"
joined_string = s1 + " " + s2  # Adding a space between the strings
print(joined_string)
```

#### 3.3 String Formatting
- **Task 3.3**: Use the `str.format()` method and f-strings to format strings with variable placeholders. Create a formatted string that includes variables for a name and age, then print the result.

```python
# Task 3.3 Code Snippet using str.format()
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Task 3.3 Code Snippet using f-string
print(f"My name is {name} and I am {age} years old.")
```

### 4. Type Conversion
Understanding how to convert between different types is essential in Python programming, especially when dealing with user input or data from different sources.

- **Task 4.1**: Convert a string that represents a number into an integer and a floating-point number. Print the results and their types.

```python
# Task 4.1 Code Snippet
string_number = "100"
int_number = int(string_number)
float_number = float(string_number)

print(int_number, type(int_number))
print(float_number, type(float_number))
```

### 5. Formatting Numbers
Properly formatted numbers are crucial for output that's readable and user-friendly, especially when dealing with large numbers or precise decimal places.

- **Task 5.1**: Format an integer with a thousands separator and print the result.

```python
# Task 5.1 Code Snippet
large_number = 123456789
formatted_number = "{:,}".format(large_number)
print(formatted_number)
```

- **Task 5.2**: Format a floating-point number to show up to two decimal places. Experiment with formatting numbers in different ways (e.g., no decimal places, thousands separator).

```python
# Task 5.2 Code Snippet
pi = 3.14159
formatted_float =