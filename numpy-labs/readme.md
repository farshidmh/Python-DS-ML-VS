### Introduction to NumPy

#### Objective:

This lab aims to introduce you to NumPy, one of the foundational libraries for data science in Python. You will learn how to create, access, manipulate, and perform operations on NumPy arrays.

#### Time to practice

Estimated time to complete: 60 minutes

#### Prerequisites:

- Basic knowledge of Python.
- Python installed on your system.
- An IDE or text editor for writing Python code.

#### Tools and Materials Needed:

- A computer with Python and NumPy installed. To install NumPy, run `pip install numpy` in your command line or terminal.

### Part 1: Introduction to NumPy

NumPy, along with SciPy, forms the foundation for data science in Python by providing efficient structures for numerical computations, especially for array and matrix operations.

#### References:

- Python Data Science Handbook, Ch 02.1: [Understanding Data Types](https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html)
- Python Data Science Handbook, Ch 02.2: [Basics of NumPy Arrays](https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html)

### Part 2: Creating NumPy Arrays

1. **Importing NumPy and Checking Version**
    ```python
    import numpy as np
    print(np.__version__)
    ```

2. **Creating Arrays**
    - Understand that to create a NumPy array, you should pass a list of numbers. For example, `np.array([1, 2, 3])` is correct, whereas `np.array(1, 2, 3)` will raise an error.
    - Create an integer array and print it:
        ```python
        a1 = np.array([1, 4, 2, 5, 3])
        print(a1)
        print(type(a1))
        ```
    - Create a float array by specifying the data type and print its type and data type:
        ```python
        a2 = np.array([1, 2, 3, 4], dtype='float32')
        print(a2)
        print(type(a2))
        print(a2.dtype)
        ```
    - Generate a sequence of numbers using `np.arange(100)` and observe the output.

### Part 3: Accessing NumPy Arrays

- Learn that NumPy arrays use zero-based indexing.
- Experiment with accessing the first element (`a[0]`), the last element (`a[-1]`), and understanding negative indexing (`a[-2]`).

### Part 4: Manipulating NumPy Arrays

- Multiply a sequence by a scalar to understand how operations are applied to each element:
    ```python
    a = np.arange(10)
    print(a * np.pi)
    ```

### Part 5: Multidimensional Arrays

- Convert a single-dimensional array into a multidimensional array using `.reshape` and access its elements. For example, `b[1,2]` accesses the element in the second row and third column.

### Part 6: Handy NumPy Array Creations

- Explore creating arrays filled with zeros, ones, or random numbers:
    ```python
    # Zeros
    np.zeros(10)
    # Ones
    np.ones(10, dtype=int)
    # Random numbers
    np.random.random(10)
    ```

### Part 7: NP Datatypes and Operations

- Understand the various data types available in NumPy and experiment with indexing and slicing arrays.

### Part 8: Benchmarking NumPy Arrays vs. Python Lists

- Use `%timeit` to compare performance between NumPy arrays and Python lists for different operations and sizes. Analyze the speed and memory footprint of both, understanding the efficiency gains with
  NumPy.

### Discussion

Reflect on your findings regarding the performance comparison between NumPy arrays and Python lists. Consider speed, memory usage, and the convenience of operations.

### Bonus Exercises

For those interested in further exploration, check out additional exercises and examples
at [guided-machine-learning/python-data-analysis/np-1__numpy-intro.md](https://github.com/elephantscale/guided-machine-learning/blob/master/python-data-analysis/np-1__numpy-intro.md).

#### Conclusion

Through this lab, you've gained a foundational understanding of NumPy, its efficiency, and its pivotal role in Python data science. Continue to explore the vast functionalities of NumPy as you
progress in your data science journey.