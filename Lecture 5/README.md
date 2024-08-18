This lecture contains a bit of a mishmash of topics to help you build a project (next time). Most of these topics are tiny and don't warrant an entire lecture but are useful to know before moving forward.

## Lecture Overview

1. **Modules and Their Importance**: Understand the concept of modules and how they enhance code organization, encompassing both built-in and third-party modules.
2. **Import Statements and Usage**: Learn how to import modules using different techniques.
3. **JSON Handling in Python**: Explore JSON as a common data format, grasp its significance, and discover how to read from and write to JSON files using Python's `json` module.
4. **Web Requests and `requests` Module**: Explore GET and POST requests, and use the `requests` module to interact with web services.

## 1. Modules in Python

### What are Modules?

In Python, modules are files containing Python definitions and statements. They help in organizing code into reusable and maintainable units. Python comes with a variety of built-in modules, and you can also install additional third-party modules using tools like `pip`.

### Examples of Built-in Modules

Python has several built-in modules that provide functionalities beyond the basic language features. Let's look at a few examples:

- `math`: Provides mathematical functions and constants.
- `random`: Generates random numbers and elements.
- `datetime`: Manipulates dates and times.
- `os`: Interacts with the operating system, e.g., file operations. (we know this one!)
- `sys`: Provides access to interpreter variables and functions.

### Examples of Third-Party Modules

Some functionalities are not included in Python's standard library but can be added using third-party modules. You can install these modules using `pip`, the Python package manager. For instance:

- `requests`: For making HTTP requests.
- `numpy`: For numerical operations.
- `pandas`: For data manipulation and analysis.

pip is a package manager for Python that allows you to install and manage software packages written in Python. You can use pip to install packages from the Python Package Index (PyPI) and other indexes. It comes pre-installed with Python 3.4 and above. For example to install the requests module, you can run:

```bash
pip install requests
```

## 2. Import Statements

### Importing Modules

To use the functionalities of a module, you need to import it using the `import` statement. Here's how:

```python
import math

result = math.sqrt(25)
print(result)  # Output: 5.0
```

### Importing with Aliases

You can use aliases to make module names shorter:

```python
import math as m

result = m.sqrt(36)
print(result)  # Output: 6.0
```

### Importing Specific Functions/Attributes

Import only specific functions or attributes from a module:

```python
from math import sqrt

result = sqrt(16)
print(result)  # Output: 4.0
```

Sometimes, you might want to import all functions and attributes from a module. While this is generally discouraged due to potential naming conflicts, you can do it like this:

```python
from math import *

result = sqrt(64)
print(result)  # Output: 8.0
```

### Importing from Other Files

Suppose you have a file named `my_module.py` with a function `my_function`. You can import and use it like this:

```python
from my_module import my_function

my_function()
```

So you can see that python modules are just python files that you can import into other python files. All libraries you use are just python files that you can import into your own code and they work the same way as the example above.

Now that we know a little bit about modules and importing, let's look at some useful modules.

## 3. JSON Handling in Python

### What is JSON?

JSON (JavaScript Object Notation) is a lightweight data interchange format widely used for data storage and communication. It uses a human-readable text format to represent data objects consisting of attribute-value pairs.

### Reading and Writing JSON Files

Python provides the `json` module for working with JSON data. Here's how to read from and write to JSON files:

```python
import json

# Reading from a JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)

# Writing to a JSON file
data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('output.json', 'w') as f:
    json.dump(data, f)
```

`data` in the above examples, is simply a python dictionary.

### 4. Web Requests and the `requests` Module

#### Understanding HTTP Requests

In the modern digital landscape, the World Wide Web functions through a protocol called HTTP (Hypertext Transfer Protocol). When you access a website, your browser sends HTTP requests to a server, which then responds with the requested data. We can also write Python programs to make the same kinds of requests. Browsers are just examples of specialized programs that deal with these requests.

Two of the most common types of HTTP requests are GET and POST.

##### GET Requests

GET requests are used to retrieve data from a server. When you enter a URL into your browser's address bar and hit Enter, you're essentially making a GET request. This type of request is used to fetch resources like web pages, images, videos, or any other data hosted on a server.

##### POST Requests

POST requests, on the other hand, are used to send data to a server to be processed. POST requests are commonly used when you submit forms on websites, make online purchases, or send data to APIs (Application Programming Interfaces) for processing.

#### The `requests` Module

The `requests` module in Python simplifies the process of making HTTP requests. It abstracts away the complexities of handling network connections, headers, and data encoding, allowing you to focus on interacting with web services.

##### Making GET Requests with `requests`

To make a GET request using the `requests` module, you provide the URL you want to request data from:

```python
import requests

response = requests.get('https://api.example.com/data')
print(response.text)  # Prints the response content
```

In this example, `response` contains information about the server's response, including the status code, headers, and the response content. What do these mean?

- Status code is a number that tells you if the request was successful or not. 200 means success, 404 means not found, 500 means server error, etc.
- Headers are metadata about the response. They can contain information about the server, the content type, the date, etc. You typically don't need to worry about these.
- Response content is the actual data you requested. It can be in many formats, but typically it's in JSON or HTML.

GET requests also allow for query parameters. These are appended to the URL after a question mark (`?`) and separated by ampersands (`&`). Query parameters are often used to filter, sort, or paginate data. For example, you might query a library's API for books with the title "Hunger Games" and limit the results to 10.

Example:

```python
import requests

# Using query parameters
response = requests.get('https://api.example.com/search?search=Hunger+Games&limit=10')
print(response.json())    # Parsed JSON response
```

but a nicer way to write the same thing in the requests module is:

```python
import requests

# Using query parameters
parameters = {'search': 'Hunger Games', 'limit': 10}
response = requests.get('https://api.example.com/search', params=parameters)
print(response.json())    # Parsed JSON response
```

##### Making POST Requests with `requests`

When making a POST request, you typically send data as part of the request's body. This is useful when submitting forms or sending data to an API:

```python
import requests

data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://api.example.com/login', data=data)
print(response.status_code)  # Prints the HTTP status code
```

Here, `data` is a dictionary containing the data you want to send. The server processes the data and responds with an appropriate status code and possibly additional data. Notice that the data is not passed in the url as with GET requests. This is because POST requests are meant to send data to the server and sometimes the data can be large or sensitive.

##### Using the response

In the examples above, `response` contains information about the server's response, including the status code, headers, and the response content. Some of the parts of the response include:

- `response.status_code`: The HTTP status code of the response. We'll understand this momentarily.
- `response.content`: The raw content of the response.
- `response.text`: The response content as a string.
- `response.json()`: Parses the response content as JSON (if applicable).

The last three are just different ways of accessing the response content. The `json()` method is particularly useful when the response content is in JSON format.

#### HTTP Status Codes

HTTP responses include status codes that provide information about the outcome of the request. These codes help you understand whether the request was successful, if there was an error, or if further action is needed. Here are some common status codes:

- 200 OK: The request was successful, and the server responded with the requested data.
- 400 Bad Request: The server couldn't understand the request due to invalid syntax or parameters.
- 404 Not Found: The requested resource couldn't be found on the server.
- 500 Internal Server Error: An error occurred on the server while processing the request.

By checking the status code in the response, you can programmatically determine the outcome of your request and take appropriate action.
Check out the [HTTP status code documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) for a comprehensive list of status codes and their meanings.

## Conclusion

In this lecture, we covered essential concepts that are fundamental to your journey in Python programming. We explored modules, import statements, JSON handling, and web requests using the `requests` module. By understanding and applying these concepts, you'll be better equipped to develop versatile and powerful Python applications.
