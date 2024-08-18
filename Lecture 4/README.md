## Lecture Overview

1. **What are functions?**: Learn the definition and purpose of functions as reusable blocks of code, their role in problem decomposition, and how they handle inputs and outputs.
2. **Writing Functions**: Explore the process of defining functions using the `def` keyword, understanding their structure, including arguments and return values.
3. **Mutable and Immutable Objects**: Dive into the distinction between mutable and immutable objects, their impact on function behavior, and how they are passed within functions.
4. **Scopes**: Understand the concept of variable scopes, ranging from local to global, and their significance in accessing and modifying variables within functions.

### 1. What is a Function?

#### 1.1. **Definition and Purpose**

A function is a reusable block of code that performs a specific task. It helps in breaking down complex problems into smaller, manageable pieces. Functions take input (arguments), perform some operations, and can optionally return a value.

#### 1.2. **Why Use Functions?**

- **Modularity**: Functions promote modularity by isolating specific tasks. This makes your code easier to read, understand, and maintain.
- **Reusability**: Once you define a function, you can use it multiple times in your program, reducing code duplication.
- **Abstraction**: Functions hide the implementation details and provide a higher-level interface to work with.

### 2. Writing Functions

```python
def greet(name: str) -> None:
    """Greets the user by name."""
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
```

- `def`: Keyword to define a function.
- `greet`: Function name.
- `name: str`: Argument with type hint.
- `-> None`: Return type hint (None indicates no return value).

#### 2.1. **Returning Values from Functions**

Functions can return values using the `return` statement.

```python
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers and returns the result."""
    result = a * b
    return result

product = multiply(5, 4)  # product = 20
```

#### 2.2. **Introduction to Optional Arguments**

Functions can have optional arguments with default values.

```python
def power(base: float, exponent: float = 2) -> float:
    """Raises the base to the exponent power."""
    return base ** exponent

print(power(3))      # 3^2 = 9
print(power(2, 3))   # 2^3 = 8
```

#### 2.3. **Using Keyword Arguments**

You can specify arguments by their parameter names.

```python
def divide(dividend: float, divisor: float) -> float:
    """Divides dividend by divisor."""
    return dividend / divisor

print(divide(divisor=2, dividend=10))  # 10 / 2 = 5.0
```

#### 2.4. **Handling Variable Number of Arguments**

Sometimes, you might not know how many arguments you need in advance. Python allows you to define functions that accept a variable number of arguments using the `*args` syntax. These arguments are collected into a tuple.

```python
def add_numbers(*args: int) -> int:
    """Adds up a variable number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3, 4))  # 1 + 2 + 3 + 4 = 10
print(add_numbers(5, 10, 15))   # 5 + 10 + 15 = 30
```

The `*args` parameter collects any number of positional arguments into a tuple. This allows you to create flexible functions that can handle varying amounts of input.

#### 2.5 **Arbitrary Keyword Arguments**

Similarly, you can use the `**kwargs` syntax to handle a variable number of keyword arguments. These arguments are collected into a dictionary.

```python
def print_info(**kwargs: str) -> None:
    """Prints information about the provided keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Wonderland")
# Output:
# name: Alice
# age: 25
# city: Wonderland
```

The `**kwargs` parameter collects any number of keyword arguments into a dictionary. This is incredibly useful when you want to pass a dynamic set of named arguments to a function.

You can mix regular arguments, `*args`, and `**kwargs` in a function's parameter list. Just remember that the order should be: regular arguments, `*args`, and then `**kwargs`.

```python
def complex_function(arg1, arg2, *args, **kwargs):
    # function body
```

Remember that `*args` and `**kwargs` are just naming conventions; you could use any valid variable name. The asterisks `*` and double asterisks `**` are what indicate the special behavior. We will dive into what the asterisks mean in a later lecture.

### 3. Mutable and Immutable Objects

#### 3.1. Immutable Objects and Passing by Value

In Python, variables are either mutable or immutable objects. Immutable objects cannot be changed after creation. When you pass an immutable object to a function, you're passing a copy of its value, not a reference.

Let's explore this with an example using immutable objects like strings and numbers:

```python
def modify_string(s: str) -> None:
    """Modifies the string and assigns a new value."""
    s = "Hello, Python!"

text = "Hello"
modify_string(text)
print(text)  # Output: Hello
```

In this example, even though we modified the string inside the function, the original string remains unchanged outside the function. This is because strings are immutable, and `s = "Hello, Python!"` created a new string object with the new value.

Similarly, for numbers:

```python
def increment_number(n: int) -> int:
    """Increments the number by 1."""
    n += 1
    return n

value = 5
new_value = increment_number(value)
print(value)      # Output: 5
print(new_value)  # Output: 6
```

In this case, the original `value` remains unchanged because numbers are also immutable.

#### 3.2. Mutable Objects and Passing by Reference

On the other hand, mutable objects can be changed after creation. When you pass a mutable object to a function, you're passing a reference to the same object. Any modifications made inside the function affect the original object outside the function.

Let's explore this with an example using a mutable object, like a list:

```python
def modify_list(lst: list) -> None:
    """Modifies the list by appending an element."""
    lst.append(42)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # Output: [1, 2, 3, 42]
```

In this example, the list was modified inside the function, and the change is reflected outside the function because lists are mutable.

Understanding the distinction between mutable and immutable objects is crucial when working with functions that modify data.

**Key Takeaway**: Mutable objects are modified in place, while immutable objects require reassignment to make changes.

## 4. Scopes

#### 4.1 **Understanding Variable Scopes**

Variables in Python have different scopes: local and global.

```python
def show_local():
    local_var = "I am local"
    print(local_var)

show_local(x)
print(local_var) # would cause an error because local_var is not accessible here
```

#### 4.2 **Global Variables and Modifying Them**

Remember, functions can access global variables, but modifying them requires the `global` keyword.

```python
global_var = "I am global"

def show_global():
    print(global_var)

def modify_global():
    global global_var
    global_var = "Modified global"

show_global()   # I am global
modify_global()
show_global()   # Modified global
```

## Conclusion

In this lecture, we covered the fundamentals of functions in Python. You've learned about defining functions, using arguments, returning values, and dealing with scopes. Functions are crucial for writing organized and efficient code. As you continue your Python journey, make sure to practice writing and using functions to enhance your programming skills.
