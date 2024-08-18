import unittest


def add(a, b):
    """Add two numbers together"""
    pass  # TODO: Implement this function


def subtract(a, b):
    """Return the absolute difference of two numbers"""
    pass  # TODO: Implement this function


def multiply(a, b):
    """Return the product of two numbers"""
    pass  # TODO: Implement this function


def add_args(*args):
    """Return the sum of all arguments. The arguments will be numbers"""
    pass  # TODO: Implement this function


def multiply_args(*args):
    """Return the product of all arguments. The arguments will be numbers"""
    pass  # TODO: Implement this function


def collate_kwargs(**kwargs):
    """
    Convert the kwargs into a list of tuples. Each tuple will have the key and value.

    For example:
    collate_kwargs(a=1, b=2) -> [('a', 1), ('b', 2)]
    collate_kwargs() -> []
    collate_kwargs(a=1, b=2, c=3) -> [('a', 1), ('b', 2), ('c', 3)]
    """
    pass  # TODO: Implement this function


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), 1)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, 1), 2)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(-1, 1), -1)

    def test_add_args(self):
        self.assertEqual(add_args(1, 2, 3), 6)
        self.assertEqual(add_args(0, 0, 0), 0)
        self.assertEqual(add_args(-1, 1, 0), 0)

    def test_multiply_args(self):
        self.assertEqual(multiply_args(1, 2, 3), 6)
        self.assertEqual(multiply_args(0, 0, 0), 0)
        self.assertEqual(multiply_args(-1, 1, 0), 0)

    def test_collate_kwargs(self):
        self.assertEqual(collate_kwargs(a=1, b=2), [("a", 1), ("b", 2)])
        self.assertEqual(collate_kwargs(), [])
        self.assertEqual(collate_kwargs(a=1, b=2, c=3), [("a", 1), ("b", 2), ("c", 3)])


if __name__ == "__main__":
    unittest.main()
