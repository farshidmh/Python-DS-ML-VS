# Strings

## Defining Strings

Strings can be defined with single quotes, double quotes and triple quotes!

```python
s1 = 'string 1'  # using single quotes
print(s1)
```

```python
s2 = "string 2"  # double quotes
print(s2)
```

```python
## multi line strings

sql = """
SELECT * 
FROM table1
WHERE x > 0
"""

print(sql)
```

## Formatting Strings

```python
name = 'Jon'
age = 20
city = 'San Jose'

# here is how we format strings
print(f"{name} is {age} years old")  # double quotes
print(f'{name} is {age} years old')  # single quotes

# even triple quoted strings
print(f"""{name} is {age} years old""")
```

```python
# You can even do expressions
print(f"{name.upper()} is {age} years old")
```

```python
## TODO print out
# Jon is 20 years old and lives in San Jose
```

## Manipulating Strings

```python
s1 = 'Hello World'

print('string length : ', len(s1))
print('uppercase : ', s1.upper())
print('lowercase : ', s1.lower())
```

## Trim Strings

`strip` function.  Also investigate `lstrip`, `rstrip` functions

```python
s = '    hi   '
s.strip()
```

```python
## TODO : try lstrip  and rstrip  functions
```

## Splitting Strings

```python
s = 'hello world, good bye world!'
words = s.split(' ')  # split by space
print(words)
```

```python
address = "123 Main St, San Jose, CA"
tokens = address.split(',')

print('tokens len:', len(tokens))
tokens
```

```python
print('street:' , tokens[0])
print('city:', tokens[1])
```

```python
print('state:', ???)
```

```python
## TODO: extract the street number only, 
## expected output: 123
## Hint: you need to further split 'street' variable
```

## Matching Strings

### Sub String

```python
s1 = 'hello'
s2 = 'hello world'
s3 = 'bye world'

if s1 in s2:
    print('s1 is in s2')
else:
    print('s1 is NOT in s2')
```

```python
if s1 in s3:
    print('s1 is in s3')
else:
    print('s1 is NOT in s3')
```

### Regex

Regex are powerful but can get complex.

You can practice online here: [regex101.com/](https://regex101.com/)

**Try to match whole words in this text**

```text
We will be there, ofcourse!
```

**Try to match US Phone numbers in this text**

```text
Our address is 123 Main St.
Our customer phone line is : 123-456-7890
Our opening hours are 9am-5pm
```

```python
s = 'hello world, good bye world!'
words1 = s.split(' ')
words1
```

```python
# TODO split string by non-alphabetic
# We need to use regex

import re

s = 'hello world, good bye world!'

words2 = re.split('[^a-zA-Z]', s) # [^a-zA-Z] means a list of characters form a to z and A to Z

words2
```

## Exercise

Print unique words from this paragraph.

```python
str = "it was the best of times \
it was the worst of times \
it was the age of wisdom \
it was the age of foolishness \
it was the epoch of belief \
it was the epoch of incredulity \
it was the season of light \
it was the season of darkness \
it was the spring of hope \
it was the winter of despair"

words = str.split()
# list of words. 
words
```

```python
# TODO: Now find the unique words
```