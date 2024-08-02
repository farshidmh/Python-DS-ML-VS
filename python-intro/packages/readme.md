### Creating a Simple Python Package Locally

#### Objective:

Learn to create and utilize a simple Python package without the need for distribution through PyPI.

#### Time to practice

30 minutes

#### Prerequisites:

- Basic knowledge of Python programming.
- Python installed on your computer.
- Familiarity with using command line interfaces (Terminal or Command Prompt).

#### Tools and Materials Needed:

- A text editor or an Integrated Development Environment (IDE).

#### Instructions:

##### Step 1: Create Your Package Directory

1. **Create a Project Folder**: This folder will contain your package and a script that uses your package. Let's name it `my_local_package_project`.
2. **Create Your Package Folder**: Inside your project folder, create another folder with your package name, e.g., `my_package`. This is where your package modules will reside.

##### Step 2: Initialize Your Package

1. **Create an `__init__.py` File**: Inside the `my_package` folder, create a file named `__init__.py`. This file can be empty, but it signals to Python that this directory is a package.
2. **Add Modules to Your Package**: Create a Python file for your module inside the `my_package` folder, e.g., `greetings.py`. In this file, you can define functions you want to include in your
   package. Here's a simple example:

`greetings.py`

```python
def say_hello(name):
    return f"Hello, {name}!"
```

##### Step 3: Use Your Package

1. **Create a Python Script Outside Your Package**: In the root of your project folder (`my_local_package_project`), create a Python script to use your package, e.g., `test_package.py`.
2. **Import and Use Your Package**: In `test_package.py`, import the module from your package and use its functions. Here's how you might do it:

`test_package.py`

```python
from my_package import greetings

print(greetings.say_hello("World"))
```

##### Step 4: Run Your Script

1. **Run Your Script**: Open your terminal or command prompt, navigate to your project directory (`my_local_package_project`), and run your script using Python. You should see the output of the
   function call.

Command:

```
python test_package.py
```

Expected Output:

```
Hello, World!
```

#### Conclusion:

Congratulations! You've successfully created a simple Python package and used it in a script. This package is now available for use anywhere within your project directory, allowing you to organize
your code into reusable modules.

#### Additional Resources:

- [Modules and Packages in Python](https://docs.python.org/3/tutorial/modules.html)
- [Python Official Documentation](https://docs.python.org/3/)

### Evaluation:

- Verify that the package and module structure is correctly set up.
- Check that the `__init__.py` file is present in your package directory.
- Ensure that the package functions are properly defined and can be successfully imported and called from another script in your project.

This guide provides a straightforward way to create and use a Python package locally, offering a foundational understanding of Python's package system for organizing and reusing code.