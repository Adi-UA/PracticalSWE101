# hw2.py

import unittest


def test_slicing(lst):
    """
    Returns a slice of the list from index 2 to 5, inclusive.
    Example:
    Input: [10, 20, 30, 40, 50, 60]
    Output: [30, 40, 50, 60]
    """
    return lst[2:6]


def test_string_slicing(s):
    """
    Returns a slice of the string from the start to index 4.
    Example:
    Input: "Hello, World!"
    Output: "Hello"
    """
    return s[:5]


def test_reverse_list(lst):
    """
    Returns a new list with the elements in reverse order.
    Example:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
    """
    return lst[::-1]


def test_reverse_string(s):
    """
    Returns a new string with the characters in reverse order.
    Example:
    Input: "Python"
    Output: "nohtyP"
    """
    return s[::-1]


def test_destructuring_list(lst):
    """
    Returns the first and last elements of a list of three elements.
    Example:
    Input: [1, 2, 3]
    Output: (1, 3)
    """
    a, _, b = lst
    return (a, b)


def test_destructuring_string(s):
    """
    Returns the first and last characters of a string of length 4.
    Example:
    Input: "abcd"
    Output: ('a', 'd')
    """
    a, _, _, d = s
    return (a, d)


def test_slicing_with_step(lst):
    """
    Returns a slice with every second element.
    Example:
    Input: [10, 20, 30, 40, 50, 60]
    Output: [10, 30, 50]
    """
    return lst[::2]


def test_slicing_with_negative_indices(lst):
    """
    Returns a slice of the list from the last three elements.
    Example:
    Input: [1, 2, 3, 4, 5, 6]
    Output: [4, 5, 6]
    """
    return lst[-3:]


class TestSlicingAndDestructuring(unittest.TestCase):

    def test_slicing(self):
        self.assertEqual(test_slicing([10, 20, 30, 40, 50, 60]), [30, 40, 50, 60])

    def test_string_slicing(self):
        self.assertEqual(test_string_slicing("Hello, World!"), "Hello")

    def test_reverse_list(self):
        self.assertEqual(test_reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_reverse_string(self):
        self.assertEqual(test_reverse_string("Python"), "nohtyP")

    def test_destructuring_list(self):
        self.assertEqual(test_destructuring_list([1, 2, 3]), (1, 3))

    def test_destructuring_string(self):
        self.assertEqual(test_destructuring_string("abcd"), ("a", "d"))

    def test_slicing_with_step(self):
        self.assertEqual(test_slicing_with_step([10, 20, 30, 40, 50, 60]), [10, 30, 50])

    def test_slicing_with_negative_indices(self):
        self.assertEqual(
            test_slicing_with_negative_indices([1, 2, 3, 4, 5, 6]), [4, 5, 6]
        )


if __name__ == "__main__":
    unittest.main()
