# Examples of recursive functions with print statemnts to help trace the logic


def factorial(n):
    print(f"Called function with n = {n}")
    if n == 0:
        retval = 1
    else:
        retval = n * factorial(n - 1)
    print(f"Called function with n = {n}, returning {retval}")
    return retval


def fibonacci(n):
    print(f"Called function with n = {n}")
    if n == 0:
        retval = 0
    elif n == 1:
        retval = 1
    else:
        retval = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"Called function with n = {n}, returning {retval}")
    return retval


def reverse_string(s):
    print(f"Called function with s = {s}")
    if len(s) == 0:
        retval = ""
    else:
        retval = reverse_string(s[1:]) + s[0]
    print(f"Called function with s = {s}, returning {retval}")
    return retval


def string_to_char_list(s):
    print(f"Called function with s = {s}")
    if len(s) == 0:
        retval = []
    else:
        retval = [s[0]] + string_to_char_list(s[1:])
    print(f"Called function with s = {s}, returning {retval}")
    return retval


def is_palindrome(s):
    print(f"Called function with s = {s}")
    if len(s) <= 1:
        retval = True
    else:
        retval = s[0] == s[-1] and is_palindrome(s[1:-1])
    print(f"Called function with s = {s}, returning {retval}")
    return retval


def main():
    # Comment and uncomment the following lines to test different functions
    # make sure you understand how each function works and how the output is generated
    n = 5
    print(f"Factorial of {n}: {factorial(n)}\n")
    print("-" * 50)

    # n = 10
    # print(f"Fibonacci sequence up to {n}: {fibonacci(n)}\n")
    # print("-" * 50)

    # s = "hello"
    # print(f"Reverse of '{s}': {reverse_string(s)}\n")

    # s = "hello"
    # print(f"String '{s}' as a list of characters: {string_to_char_list(s)}\n")
    # print("-" * 50)

    # s = "racecar"
    # print(f"Is '{s}' a palindrome? {is_palindrome(s)}")
    # print("-" * 50)

    # s = "hello"
    # print(f"Is '{s}' a palindrome? {is_palindrome(s)}")
    # print("-" * 50)


if __name__ == "__main__":
    main()
