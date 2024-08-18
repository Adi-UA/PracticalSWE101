This lecture is a little shorter than usual, but recursion is worth spending some time on because it can take some time to wrap your head around. But we'll make it easy by taking it one step at a time.

## Lecture Overview

1. **Recursion Defined**: Recursion is a programming technique solving problems by repeatedly breaking them down into smaller instances of the same problem, eventually reaching a base case.
2. **Essential Components**: Recursive functions consist of a base case, defining when recursion stops, and a recursive case, where the function calls itself with modified inputs.
3. **Examples of Recursion**
4. **Recursion vs. Loops**: Explore the interchangeability between recursion and loops in problem-solving, showcasing both approaches' advantages.

### 1. What is Recursion?

Recursion is a programming technique where a function calls itself to solve a problem. It's like a puzzle-solving approach where a problem is broken down into smaller instances of itself. Each smaller instance is solved in a similar manner until a base case is reached, which is the simplest form of the problem that can be solved directly. In other words, when a problem can be solved by solving smaller versions of itself, we can recurse and solve the smaller problems thereby solving the big problem.

### 2. Essential Parts of a Recursive Function

A recursive function typically consists of two main components:

1. **Base Case**: This is the condition that specifies when the recursion should stop. It's the simplest scenario where the function can provide a direct answer without making further recursive calls.

2. **Recursive Case**: This is where the function calls itself with modified inputs to break down the problem into smaller instances.

### 3. Examples of Recursive Functions

Example 1: Factorial Calculation
Calculating the factorial of a number.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

Here, we start by calling `factorial(n)` which calls `factorial(n-1)` which calls `factorial(n-2)` and so on until we reach the base case of `n == 0` where we return 1. Then we start multiplying the results as we unwind the recursion. It is important to understand that the base case is crucial to prevent infinite recursion. It is also important to understand that we first recurse to the base case and then start unwinding the recursion to build the solution. This is a common pattern in recursion. It takes some time to get used to this pattern but once you do, it becomes very powerful.

Let's trace this for `n = 3`:

```
factorial(3) # first call
3 * factorial(2) # second call
3 * (2 * factorial(1)) # third call
3 * (2 * (1 * factorial(0))) # fourth call
3 * (2 * (1 * 1)) # now we hit the base case and finally start building the solution
3 * (2 * 1) # unwinding the recursion
3 * 2 # unwinding the recursion
6 # output once we have reached the top of the recursion
```

Remember that a function calling itself is no different from a function calling another function. The only difference is that the function is calling itself. So in your head, you can think of it as a function calling another function. This will help you understand recursion better. if you're having trouble understanding recursion, reach out to the instructor for help.

Example 2: Fibonacci Sequence
Generating the nth Fibonacci number.

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

Again, a useful thinking pattern is that "The current fibonacci number I am trying to calculate (n) is just the sum of factorial(n-1) and factorial(n-2)". Forget about the fact that the function is calling itself. Just think of it as a function calling another function. This will help you understand recursion better. It is not different than saying sum_of_a_and_b = a + b. It is just that a and b are calculated by calling the same function in this case.

Example 3: Sum of List
Calculating the sum of elements in a list.

```python
def list_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + list_sum(lst[1:])
```

Example 4: Power Calculation
Calculating the result of x raised to the power of n.

```python
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
```

Example 5: Palindrome Check
Checking if a string is a palindrome.

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
```

### 4. Conversion between Recursion and Loops

All recursive functions can be implemented using loops, and vice versa. This is a theoretical concept known as the Church-Turing thesis. However, in practice, some problems are more naturally solved using recursion, while others are better suited for loops.

Recursion provides an elegant and intuitive way to solve problems by breaking them down into smaller parts. On the other hand, loops provide a more iterative approach that can sometimes be more efficient.

For example, the factorial calculation using a loop:

```python
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

Both approaches have their strengths and weaknesses, and choosing between them depends on the specific problem and readability of the code.

## Conclusion

Recursion is a powerful technique that allows us to solve complex problems by breaking them down into simpler instances. Understanding the base case and recursive case is crucial for writing effective recursive functions. Additionally, knowing how to convert between recursion and loops provides flexibility in problem-solving approaches.
