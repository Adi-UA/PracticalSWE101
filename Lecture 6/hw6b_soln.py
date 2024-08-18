def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Example:
    factorial(5) -> 120

    :param n: Integer for which to calculate the factorial (n >= 0)
    :return: Factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """
    Compute the nth Fibonacci number using recursion.

    Example:
    fibonacci(6) -> 8

    :param n: Integer (n >= 0) representing the index in the Fibonacci sequence
    :return: The nth Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_list(lst):
    """
    Sum the elements of a list using recursion.

    Example:
    sum_list([1, 2, 3, 4]) -> 10

    :param lst: List of numbers to sum
    :return: Sum of all elements in the list
    """
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


def reverse_string(s):
    """
    Reverse a string using recursion.

    Example:
    reverse_string("hello") -> "olleh"

    :param s: String to be reversed
    :return: Reversed string
    """
    if len(s) == 0:
        return ""
    else:
        return reverse_string(s[1:]) + s[0]


def is_palindrome(s):
    """
    Check if a string is a palindrome using recursion.

    Example:
    is_palindrome("racecar") -> True

    :param s: String to check
    :return: True if the string is a palindrome, False otherwise
    """
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


def gcd(a, b):
    """
    Find the greatest common divisor (GCD) of two numbers using recursion.

    Example:
    gcd(48, 18) -> 6

    :param a: First integer
    :param b: Second integer
    :return: GCD of a and b
    """
    if b == 0:
        return a
    else:
        return gcd(
            b, a % b
        )  # because whatever can divide b must also divide a % b, which is the leftover of a divided by b


def sum_of_digits(n):
    """
    Calculate the sum of digits of a number using recursion.

    Example:
    sum_of_digits(1234) -> 10

    :param n: Integer (n >= 0)
    :return: Sum of the digits of n
    """
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)


def count_occurrences(lst, target):
    """
    Count the occurrences of a specific element in a list using recursion.

    Example:
    count_occurrences([1, 2, 3, 2, 2], 2) -> 3

    :param lst: List of elements
    :param target: Element to count occurrences of
    :return: Number of times target appears in lst
    """
    if len(lst) == 0:
        return 0
    else:
        return (lst[0] == target) + count_occurrences(lst[1:], target)


def find_max(lst):
    """
    Find the maximum element in a list using recursion.

    Example:
    find_max([1, 4, 5, 2]) -> 5

    :param lst: List of numbers
    :return: Maximum element in lst
    """
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))


def flatten(lst):
    """
    Flatten a nested list using recursion.

    Example:
    flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]

    :param lst: List that may contain nested lists
    :return: A flat list with no nested elements
    """
    if len(lst) == 0:
        return []
    elif isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])


# Unit Test for the Exercise
import unittest


class TestRecursiveFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120, "Failed factorial test")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 8, "Failed Fibonacci test")

    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3, 4]), 10, "Failed sum list test")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh", "Failed reverse string test")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"), "Failed palindrome test")
        self.assertFalse(is_palindrome("hello"), "Failed palindrome test")

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6, "Failed GCD test")

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(1234), 10, "Failed sum of digits test")

    def test_count_occurrences(self):
        self.assertEqual(
            count_occurrences([1, 2, 3, 2, 2], 2), 3, "Failed count occurrences test"
        )

    def test_find_max(self):
        self.assertEqual(find_max([1, 4, 5, 2]), 5, "Failed find max test")

    def test_flatten(self):
        self.assertEqual(
            flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5], "Failed flatten test"
        )


if __name__ == "__main__":
    unittest.main()
