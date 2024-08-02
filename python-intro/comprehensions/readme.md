# Comprehensions

## Objective
Explore comprehension in Python, a concise and powerful way to create lists, dictionaries, and sets.

## Time to Complete

30 minutes

## 1 - Build a list of squares

### 1.1: Standard for loop

```python
a = [1, 2, 3, 4, 5]
b = []

for x in a:
    b.append(x * x)

b
```

### 1.2 - Use list comprehension

```python
b = [x*x for x in a]  # <--- here is comprehension.  very compact, eh?

b
```

## 2 - Process words in a sentence

```python
words = ['Sun', 'rises', 'in', 'the', 'East']
print(words)
```

```python
# First, copy the words
words2 = [w for w in words]
print(words2)
```

```python
# Convert to uppercase
words2 = [w.upper() for w in words]
print(words2)
```

```python
# Reverse the words
words2 = [w[::-1] for w in words]
print(words2)
```

## Exercise

Create reversed, uppercase strings.

```python
words = ['Sun', 'rises', 'in', 'the', 'East']
words3 = [w[::-1].upper() for w in words]
words3
```