## Multithreading in Python Lab

Welcome to the Multithreading lab in Python! In this lab, we will explore the concept of multithreading, which allows us to perform multiple tasks concurrently within a single process.

### Objectives

- Understand the basics of multithreading and its advantages.
- Learn how to create and manage threads in Python using the `threading` module.
- Explore synchronization techniques such as locks and semaphores.
- Practice implementing multithreading in Python to improve performance and responsiveness.

### Time to Code

Appropriate time to spend in this lab is 45 minutes.

### 1. Introduction to Multithreading

Multithreading is a programming concept that allows multiple threads of execution to run concurrently within a single process. This enables better utilization of CPU resources and improves the responsiveness of applications, especially in I/O-bound tasks.

### 2. Creating Threads in Python

In Python, we can create and manage threads using the `threading` module. Threads are represented by `Thread` objects, which can execute target functions concurrently.

#### Example:

```python
import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")

def print_letters():
    for letter in 'abcde':
        print(f"Thread 2: {letter}")

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Threads execution completed!")
```

### 3. Synchronization

When multiple threads access shared resources concurrently, synchronization mechanisms are required to prevent race conditions and ensure data integrity. Python provides several synchronization primitives such as locks, semaphores, and conditions.

#### Example:

```python
import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

def decrement_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter -= 1

# Create two threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=decrement_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("Counter:", counter)
```

### Instructions

1. Implement a multithreaded program that simulates concurrent downloading of multiple files from a remote server. Each thread should download a different file simultaneously.
2. Use synchronization techniques to prevent race conditions when accessing shared resources such as a global counter or a shared data structure.
3. Experiment with different synchronization primitives such as locks, semaphores, and conditions to observe their effects on thread synchronization and performance.
4. Measure the execution time of your multithreaded program and compare it with a single-threaded version to evaluate the performance gains achieved through multithreading.

Follow the instructions and experiment with multithreading in Python to gain a deeper understanding of concurrent programming concepts. Happy threading!