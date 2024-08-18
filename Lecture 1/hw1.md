# Homework Assignment 1

## Before You Begin

### Set Up Your Environment

1. **Install Python** (if you haven't already):

   - You can download and install Python from [python.org](https://www.python.org/downloads/).
   - Follow the installation instructions for your operating system.

2. **Get a Text Editor or IDE:**
   - Download and install a text editor or an Integrated Development Environment (IDE) for writing Python code. Preferably, use [Visual Studio Code](https://code.visualstudio.com/) for its simplicity and ease of use.

## Section 1: Take the Quiz

For this assignment, you'll begin by testing your knowledge of basic types and operators in Python. The quiz has been provided in the `quiz1.py` file.

### Instructions:

1. **Download the Quiz File:**

   - Ensure you have downloaded the `quiz1.py` file provided to you. It should already exist in your course materials.

2. **Run the Quiz:**

   - Open a terminal (or command prompt) in the folder where the `quiz1.py` file is located.
   - Run the Python quiz by typing:
     ```bash
     python quiz1.py
     ```
   - Answer each question as prompted. At the end of the quiz, the program will display your score along with the correct answers.

3. **Review Your Results:**
   - Analyze your score and review the questions you missed (if any). If necessary, go back and study the sections of the lecture related to those topics.

---

## Section 2: Write Your First Python Program

Now it's time to write your first Python program! This section will guide you through practicing everything covered in the lecture, including variable types, operators, and simple string manipulations.

### Step 2: Write Your First Program

We will now guide you through writing your first program. You'll practice variable types, arithmetic operations, and string manipulations.

### 2.1: Declare Variables of Different Types

Create variables for an integer, a float, and a boolean:

```python
# Variables
my_integer = 42
my_float = 3.14
my_boolean = True

# Print them out to the console
print("Integer:", my_integer)
print("Float:", my_float)
print("Boolean:", my_boolean)
```

### 2.2: Perform Arithmetic Operations

Practice arithmetic operators like addition, multiplication, division, and integer division:

```python
# Arithmetic Operations
x = 10
y = 3

sum_result = x + y
diff_result = x - y
prod_result = x * y
div_result = x / y
int_div_result = x // y

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", prod_result)
print("Division:", div_result)
print("Integer Division:", int_div_result)
```

### 2.3: Use String Manipulations

Create and manipulate strings. Concatenate two strings, multiply them, and format the output:

```python
# String Manipulations
greeting = "Hello"
name = "Alice"

# Concatenation
message = greeting + " " + name
print("Concatenated Message:", message)

# Repetition
repeated_message = greeting * 3
print("Repeated Message:", repeated_message)

# Using f-strings for formatting
formatted_message = f"{greeting}, {name}! Welcome to Python."
print("Formatted Message:", formatted_message)
```

### 2.4: Practice Boolean Logic

Use Boolean operators (`and`, `or`, `not`) in your program:

```python
# Boolean Logic
a = True
b = False

result_and = a and b
result_or = a or b
result_not = not a

print("Result of AND:", result_and)
print("Result of OR:", result_or)
print("Result of NOT:", result_not)
```

### Step 3: Running Your Program from the Terminal

1. **Save Your Python Program:**

   - Save your program as `first_program.py`.

2. **Run Your Program from the Terminal:**
   - Open your terminal and navigate to the directory where your `first_program.py` file is saved.
   - Run the Python program by typing the following command in your terminal:
     ```bash
     python first_program.py
     ```
   - The program will execute, and you will see the results printed to the console.

### Step 4: Reflect and Explore

- Review your program output. Experiment with changing variable values or adding new features to your code.
- For additional practice, create new variables, perform more arithmetic operations, or experiment with different string methods like `.upper()` or `.replace()`.

---

### Submission Instructions:

- Once you've completed both sections, submit your Python files (`quiz1.py` and `first_program.py`) along with your quiz results via email.

Happy coding! If you encounter any issues or have questions, don't hesitate to ask for help.
