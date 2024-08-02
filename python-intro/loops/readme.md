# Python Loops

## Objective
Learn about loops in Python, including `for` loops and `while` loops. Understand how to iterate over sequences and perform repetitive tasks efficiently.

## Introduction
Loops are essential in programming for executing a block of code repeatedly. Python provides two main types of loops: `for` loops and `while` loops.

## Time to Complete

30 minutes


## 1 - For Loop

- The `for` loop iterates over a sequence of values.
- The syntax consists of the keyword `for`, a variable name (often `i`), the keyword `in`, and a sequence (such as a list).
- Indented code within the loop is executed for each value in the sequence.

```python
for i in [1, 2, 3]:
    print(i)
```

### Spaces Matter!

Indentation is crucial in Python, as it defines the scope of code blocks.

```python
for i in [1, 2, 3]:
    print(i)
    print(i)
```

```python
for i in [1, 2, 3]:
    print(i)
print(i)
```

### 1.1 - Range

The `range()` function generates a sequence of integers up to a specified value (non-inclusive).

```python
for i in range(10):
    print(i)
```

### 1.2 - Odd/Even

You can determine whether a number is odd or even using the modulo operator (`%`).

```python
# Print numbers from 0 to 19 along with their odd/even status
for number in range(20):
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
```

## 2 - While loops

While loops are used when the number of iterations is non-deterministic.

### 2.1 - Countdown

A typical use case for a while loop is counting down from a starting number.

```python
n = 10
while n > 0:
    print(n)
    n -= 1
print('blast off!')
```

### 2.2 - Guessing Game

In this example, the loop continues until the user enters a negative number.

```python
input_number = int(input('Enter a number: '))

while input_number >= 0:
    print("You entered:", input_number)
    input_number = int(input('Enter a number: '))

print("Negative number entered, exiting the loop")
```

## 3 - Looping Through Lists

To iterate over a list, use the `for x in LIST` syntax.

```python
a = [1, 2, 3, "hi", "bye"]
for x in a:
    print(x)
```

## 4 - Looping Through Dictionaries

You can iterate over dictionaries using their keys or key-value pairs.

```python
d = {'name': 'Tim', 'age': 20, 'phone': '123-456-789'}

# Option 1: Iterate using keys
for k in d.keys():
    print('key:', k)
    print('value:', d[k])

# Option 2: Iterate using items
for k, v in d.items():
    print(k, v)
```

## Exercise 1

Create a guessing game where the user must guess a random number between 1 and 10.

```python
import random

magic_number = random.randint(1, 10)
user_guess = 0

while magic_number != user_guess:
    user_guess = int(input("Guess a number: "))
    
    if user_guess > magic_number:
        print("Too high!")
    elif user_guess < magic_number:
        print("Too low!")
    else:
        print("You guessed it!", magic_number)
        break

print("Thanks for playing!")
```

## Bonus Exercises

Explore additional exercises and challenges in Python control structures [here](https://github.com/elephantscale/guided-machine-learning/blob/master/python/4-control.md).