# Functions

Python allows us to create functions. We are going to see how to do that.

## Time to Complete

30 minutes

## 1 - Python Functions

### 1.1 - No return functions

```python
# Simple function with one input and NO return value
def say_hi(name):
    print('Hi ', name)

say_hi("Bob")  # Should print "Hi Bob"
```

### 1.2 - One return value

```python
# Simple function with two inputs and 1 return value
def mymax(first, second):
    if first > second:
        return first
    else:
        return second

print(mymax(1, 2))  # Should print "2"
```

```python
# This function returns nothing!
## TODO: Fix the bug!

def my_upper(str):
    str.upper()

print(my_upper('hi'))
```

### 1.3 - More than one return value

Python uses tuples to return multiple things from a function

```python
def plus_minus_one(n):
    return (n-1, n, n+1)

ret = plus_minus_one(10)
ret
```

We can capture individual returns into variables like this

```python
(x, y, z) = plus_minus_one(100)
print(x)
print(y)
print(z)
```

```python
# Brackets are optional

x, y, z = plus_minus_one(100)
print(x)
print(y)
print(z)
```

## 2 - Lambda Functions

Lambda functions are anonymous functions, short one-liners that we pass as arguments without.

```python
## Full-fledged function

def my_square(x):
    return x*x
    
print(my_square(10))
```

```python
# We can define simple functions using lambda functions

my_square2 = lambda x: x*x

print(my_square2(11))
```

### 2.1 - Functions in Comprehensions

As a matter of fact when we used list comprehensions, we used lambda (anonymous) functions

```python
# Defining an expression on the fly

[x*x for x in range(1, 10+1)]
```

```python
## Calling the 'regular' function

[my_square(x) for x in range(1, 10+1)]
```

```python
## Calling the 'lambda' function

[my_square2(x) for x in range(1, 10+1)]
```

```python
# Sort by second value

names = [(1, 'Mary'), (2, 'Bob'), (3, 'Zahra'), (4, 'Lu')]
names.sort(key=lambda name_pair: name_pair[1])
names
```

## Exercises

### Exercise - 1

Trying out functions

```python
# Now it is your turn. Try to experiment by creating a function yourself,
# and then calling it.

# Here is something to convert fahrenheit to celsius 
# (To convert temperatures in degrees Fahrenheit to Celsius, subtract 32 and multiply by 5/9)

# TODO: complete the function
def convert_F_to_C(f):
    return 0

temp_f = [35, 45, 56, 60, 70, 80, 90, 100]

## TODO
temp_c = [convert_F_to_C(f) for f in temp_f]
print(temp_c)
```

```python
## TODO: Define the function using 'lambda' expression and try it

convert_F_to_C_2 = lambda x: 0

[convert_F_to_C_2(f) for f in temp_f]
```

```python
## TODO: do it with an expression

[0 for f in temp_f]
```