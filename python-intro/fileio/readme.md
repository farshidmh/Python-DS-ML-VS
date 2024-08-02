## File IO Lab

In this lab, you will learn how to perform basic file input and output operations in Python. You will explore reading from a file, writing to a file, and appending to a file.

## Time to Complete

30 minutes

### Reading from File

To read from a file, you can use the `with` clause in Python, which ensures that the file is properly closed after reading. You can open a file in read mode (`'r'`) and use the `read()` function to read the entire contents of the file into a string.

```python
with open("example-1.txt", "r") as f:
    contents = f.read()
print(contents)
```

To read the file line by line, you can use a `for` loop with the file object. Each iteration of the loop will read one line from the file.

```python
with open("example-1.txt", "r") as f:
    line_number = 0
    for line in f:
        line_number +=1
        print(line_number, line)
```

### Writing to File

To write to a file, you can open the file in write mode (`'w'`) and use the `write()` function to write contents to the file.

```python
contents = """Hello world!
"""
with open("example-2.txt", "w") as f:
    f.write(contents)
```

### Appending to a File

To append to a file, you can open the file in append mode (`'a'`) and use the `write()` function to add contents to the end of the file.

```python
with open("example-2.txt", "a") as f:
    f.write("Goodbye, world!")
```

After writing or appending to the file, you can read the file to verify the changes.

```python
with open("example-2.txt", "r") as f:
    contents = f.read()
print(contents)
```

Now, proceed with the above instructions and experiment with file input and output operations in Python.