import unittest
from typing import Dict, List, Set


# Task 1: Write a function that checks if a number is positive, negative, or zero.
def check_number_sign(number: int) -> str:
    # TODO: Write an if-else statement to check if the number is positive, negative, or zero.
    # Expected output: "positive", "negative", or "zero"
    result: str = None  # Store the result in this variable
    return result


# Task 2: Write a function that returns a list of squares from 1 to n.
def squares_up_to_n(n: int) -> List[int]:
    squares: List[int] = []  # This will hold the squares
    # TODO: Write a for loop to append the squares of numbers from 1 to n to the list 'squares'.
    return squares


# Task 3: Write a function that counts down from a given number to zero.
def countdown(number: int) -> List[int]:
    countdown_list: List[int] = []  # This will hold the countdown values
    # TODO: Write a while loop that appends the countdown numbers to countdown_list.
    return countdown_list


# Task 4: Write a function that creates a list of even numbers from a given list.
def filter_even_numbers(numbers: List[int]) -> List[int]:
    # TODO: Write a list comprehension that filters out even numbers from the list 'numbers'.
    return []


# Task 5: Write a function that creates a new dictionary with squares of numbers as values.
def square_dict(numbers: List[int]) -> Dict[int, int]:
    # TODO: Write a dictionary comprehension that maps each number to its square.
    return {}


# Task 6: Write a function that doubles an integer value.
def double_integer(value: int) -> int:
    double_value: int = None  # Store the double value in this variable
    return double_value


# Task 7: Write a function that appends a greeting to each name in a list.
def greet_names(names: List[str]) -> List[str]:
    greetings: List[str] = []  # This will hold the greeting messages
    # TODO: Write a for loop that appends "Hello, {name}!" for each name in 'names'.
    return greetings


# Task 8: Write a function that uses enumerate to create a list of indexed names.
def indexed_names(names: List[str]) -> List[str]:
    indexed_names: List[str] = []  # This will hold the indexed names
    # TODO: Use enumerate to append strings like "Index 0: Alice" to 'indexed_names'.
    return indexed_names


# Task 9: Write a function to calculate the sum of numbers from 1 to n. You must not use the formula n * (n + 1) // 2.
# Look up the range() and sum() functions.
def sum_to_n(n: int) -> int:
    sum_result: int = 0  # This will hold the sum
    # TODO: Use a while loop to calculate the sum of numbers from 1 to n.
    return sum_result


# Task 10: Write a function that creates a set of unique lengths of words in a list.
def unique_word_lengths(words: List[str]) -> Set[int]:
    # TODO: Write a set comprehension to find the unique lengths of words in the list 'words'.
    return set()


# Unit tests to verify the solutions
class TestHomeworkAssignment(unittest.TestCase):

    def test_task_1(self):
        self.assertEqual(check_number_sign(5), "positive")
        self.assertEqual(check_number_sign(-3), "negative")
        self.assertEqual(check_number_sign(0), "zero")

    def test_task_2(self):
        self.assertEqual(squares_up_to_n(3), [1, 4, 9])
        self.assertEqual(squares_up_to_n(5), [1, 4, 9, 16, 25])

    def test_task_3(self):
        self.assertEqual(countdown(3), [3, 2, 1, 0])
        self.assertEqual(countdown(5), [5, 4, 3, 2, 1, 0])

    def test_task_4(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_even_numbers([10, 15, 20]), [10, 20])

    def test_task_5(self):
        self.assertEqual(square_dict([1, 2, 3]), {1: 1, 2: 4, 3: 9})
        self.assertEqual(square_dict([4, 5]), {4: 16, 5: 25})

    def test_task_6(self):
        self.assertEqual(double_integer(4), 8)
        self.assertEqual(double_integer(0), 0)

    def test_task_7(self):
        self.assertEqual(
            greet_names(["Alice", "Bob"]), ["Hello, Alice!", "Hello, Bob!"]
        )

    def test_task_8(self):
        self.assertEqual(
            indexed_names(["Alice", "Bob"]), ["Index 0: Alice", "Index 1: Bob"]
        )

    def test_task_9(self):
        self.assertEqual(sum_to_n(3), 6)
        self.assertEqual(sum_to_n(5), 15)

    def test_task_10(self):
        self.assertEqual(unique_word_lengths(["apple", "banana", "pears"]), {5, 6})
        self.assertEqual(unique_word_lengths(["hi", "hello", "hey"]), {2, 3, 5})


if __name__ == "__main__":
    unittest.main()
