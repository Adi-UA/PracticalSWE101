import unittest


def check_number_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def squares_up_to_n(n):
    squares = [i**2 for i in range(1, n + 1)]
    return squares


def countdown(number):
    countdown_list = []
    while number >= 0:
        countdown_list.append(number)
        number -= 1
    return countdown_list


def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def square_dict(numbers):
    return {num: num**2 for num in numbers}


def double_integer(value):
    return value * 2


def greet_names(names):
    return [f"Hello, {name}!" for name in names]


def indexed_names(names):
    return [f"Index {i}: {name}" for i, name in enumerate(names)]


def sum_to_n(n):
    return sum(range(1, n + 1))


def unique_word_lengths(words):
    return {len(word) for word in words}


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
