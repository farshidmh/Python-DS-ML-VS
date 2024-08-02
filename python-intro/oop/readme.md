## OOP in Python Lab

Welcome to the Object-Oriented Programming (OOP) lab in Python! In this lab, we will explore advanced concepts of OOP by creating and working with classes in Python.

### Objectives

- Understand how to define classes and instantiate objects.
- Learn about class attributes, instance attributes, and methods.
- Explore inheritance and class hierarchy.
- Practice accessing attributes and calling methods of objects.


### Time to Code

Appropriate time to spend in this lab is 45 min.

### 1. Defining a Class

Let's start by defining a class called `Door`. Each `Door` object will have the following attributes:

- `number`: representing the door number (e.g., 1, 2, 3, etc.).
- `status`: indicating whether the door is open, closed, or locked.
- `material`: representing the material of the door (e.g., wood, metal, etc.).

We will also define methods to open and close the door, as well as a method to change the material of the door.

```python
class Door:
    def __init__(self, number, status, material='wood'):
        """
        Constructor to initialize door number, status, and material.
        """
        self.number = number
        self.status = status
        self.material = material
    
    def open(self):
        """
        Method to open the door.
        """
        if self.status != 'locked':
            self.status = 'open'
        else:
            print("Cannot open the door. It's locked!")
    
    def close(self):
        """
        Method to close the door.
        """
        self.status = 'closed'
    
    def change_material(self, new_material):
        """
        Method to change the material of the door.
        """
        self.material = new_material
```

### 2. Instantiating a Class

To create an instance of a class (an object), we use the class name followed by parentheses containing any required parameters. For example:

```python
my_door = Door(1, 'closed', 'metal')
```

### 3. Accessing Attributes and Calling Methods

We can access attributes and call methods of an object using dot notation. For instance:

```python
print(my_door.number)  # Accessing the door number attribute
my_door.open()          # Calling the open() method
```

### 4. Class Attributes and Class Methods

Class attributes and methods are common to all instances of a class. They are defined using the `@classmethod` annotation. For example:

```python
class Door:
    color = 'brown'  # class attribute
    
    @classmethod
    def knock(cls):  # class method
        print('Knock, Knock!')
```

We can access class attributes and call class methods either from an instance of the class or the class itself.

```python
print(my_door.color)  # Accessing class attribute
Door.knock()          # Calling class method
```

### 5. Inheritance

Python supports inheritance, where a new class can inherit attributes and methods from a base class. For instance:

```python
class SecurityDoor(Door):
    pass  # Inherits from Door class
```

### Instructions

1. Instantiate a `Door` object with door number 1, status 'closed', and material 'wood'.
2. Check the type of the `Door` object.
3. Open the door.
4. Verify that the door is open.
5. Close the door.
6. Verify that the door is closed.
7. Access the `color` class attribute of the `Door` class.
8. Call the `knock()` class method of the `Door` class.
9. Create a `SecurityDoor` object with door number 2, status 'closed', material 'metal', and locked.
10. Attempt to open the `SecurityDoor`. Observe the behavior.
11. Instantiate another `SecurityDoor` object with door number 3, status 'closed', material 'wood', and unlocked. Then, open the door.

Follow the above instructions and experiment with object-oriented programming concepts in Python. Have fun coding!