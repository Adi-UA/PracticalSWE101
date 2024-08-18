## Lecture Overview

1. **If-else Statements**: Make decisions based on conditions to create adaptable code paths.
2. **For Loops**: Iterate through sequences efficiently, including reversing and using `range`, and `enumerate`.
3. **While Loops**: Execute code while conditions are met, mastering dynamic repetition.
4. **Building with Comprehension**: Create lists, sets, and dictionaries succinctly using loop techniques.
5. **Common Subtle Errors**: Identify and avoid pitfalls to write reliable code and enhance debugging skills.

## 1. If-else Statements

Conditional statements allow us to make decisions in our code. The most basic form is the if-else statement.

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

Common error:

```python
age = "18"  # Mistakenly using a string instead of an integer
if age >= 18:  # This will cause a TypeError
    # ...
```

## 2. Loops

### 2.1 For Loops

For loops help us iterate over a sequence of items, such as a list, and perform a task for each item.

Using `range`:

```python
for i in range(5):  # Iterates from 0 to 4
    print(i)
```

This is very useful when you need to iterate a specific number of times.

Using `in`:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

This is useful when you need to iterate over the items in a list.

Iterating in Reverse:

```python
for i in range(5, 0, -1):  # Iterates from 5 to 1 in reverse
    print(i)
```

here range(5, 0, -1) means that the loop will start at 5, end at 1, and decrement by 1. The start value is inclusive, and the end value is exclusive, so the loop will run from 5 to 1 and not include 0.

Using `enumerate`:

```python
names = ["Alice", "Bob", "Charlie"]
for items in enumerate(names):
	index = items[0]
	name = items[1]
    print(f"Person {index + 1}: {name}")
```

This is useful when you need both the index and the item in the list.

### 2.2 While Loops

While loops keep executing a block of code as long as a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

The `break` and `continue` keyword work in the same way here.

Common error:

```python
while True:
    # ...
```

Creating an infinite loop accidentally.

### 2.3 `break` and `continue`

The `break` and `continue` statements are used to control the flow of execution within loops. These statements can help you control whether to exit the loop prematurely (`break`) or skip the rest of the current iteration and move on to the next one (`continue`).

The `break` statement is used to terminate the loop prematurely when a certain condition is met. When encountered, the loop immediately exits, and the program continues executing the code following the loop. Example:

```python
for num in range(10):
	if num == 5:
		break
		print(num)
print("Loop ended.")
```

In this example, the loop prints numbers from 0 to 4, and when `num` becomes 5, the `break` statement is executed, and the loop terminates.

The `continue` statement is used to skip the rest of the current iteration and move on to the next iteration of the loop. The loop continues to run, but the remaining code within the loop block for the current iteration is skipped. Example:

```python
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
print("Loop ended.")
```

In this example, the loop prints only the odd numbers (1, 3, 5, 7, 9) by using the `continue` statement to skip even numbers.

## 4. Building with Loops: Comprehension

List comprehension allows creating lists in a concise way.

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

Set and dict comprehension work similarly for sets and dictionaries.

Common error:

```python
squared = [x**2 for x in range(1, 6)]
squared = {x**2 for x in range(1, 6)}  # Syntax for creating a set, not a list
```

You can also use conditions with list comprehension.

```python
# List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("Even Squares:", even_squares)  # Output: [4, 16, 36, 64, 100]

# Set Comprehension
word = "pythonprogramming"
unique_vowels = {char for char in word if char in 'aeiou'}
print("Unique Vowels:", unique_vowels)  # Output: {'o', 'a', 'i'}

# List Comprehension with Conditional Expression
grades = [85, 90, 78, 95, 60, 70]
pass_fail = ['Pass' if score >= 70 else 'Fail' for score in grades]
print("Pass/Fail:", pass_fail)  # Output: ['Pass', 'Pass', 'Pass', 'Pass', 'Fail', 'Pass']
```

## 5. Subtle Errors in Control Flow

While control flow constructs are powerful, they can also lead to subtle errors if not used correctly. Let's explore a couple of common mistakes and how to avoid them.

### 1. Inconsistent Loop Length Modification

```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers.remove(numbers[i])  # Mistakenly tries to remove even numbers from the list
```

In this example, the intention is to remove even numbers from the list. However, modifying the list's length within the loop by using `remove` can lead to skipping elements and unexpected behavior. This issue can be avoided by creating a new list or using techniques like list comprehension.

### 2. Wrong Order of Conditions

```python
for num in range(1, 21):
    if num % 3 == 0:
        print("Foo")  # Intended for multiples of 3
    if num % 5 == 0:
        print("Bar")  # Intended for multiples of 5
    if num % 15 == 0:
        print("Buzz")  # Intended for multiples of 15
```

In this case, we're trying to print "Foo" for multiples of 3, "Bar" for multiples of 5, and "Buzz" for multiples of 15. However, since the conditions are evaluated independently, the order can result in incorrect output. For instance, if a number is a multiple of both 3 and 5, it will print "Foo", "Bar", and "Buzz" instead of just "Buzz". To fix this, consider using `elif` to ensure only one condition is met for each number. Also, consider the order of conditions to avoid unintended behavior. The correct order should be multiples of 15 first, followed by 3 and 5.

### 3. Off-by-One Indexing Error

```python
items = [10, 20, 30, 40, 50]
for i in range(len(items)):
    print(items[i+1])  # Mistakenly prints the next element in the list
```

In this example, the intention is to print the element next to the current one in the list. However, using `i+1` can lead to an IndexError in the last iteration since there's no element after the last one. To achieve the intended behavior, consider using `i` to access the current element and `i+1` to access the next element.

## Conclusion

Control flow constructs are powerful tools, but they can introduce subtle errors if not used carefully. By being mindful of loop modifications, condition orders, and indexing, you can avoid common pitfalls and write more reliable code. Debugging and practice play a crucial role in mastering control flow concepts and producing error-free programs.
