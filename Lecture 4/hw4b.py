# exercise_mutable_types.py


# TODO: Modify the list by adding an element (do not return the list)
def add_element_to_list(lst, element):
    """
    Modify the list by adding 'element' to it.
    This function should NOT return anything.

    :param lst: The list to be modified
    :param element: The element to add to the list
    """
    pass  # TODO: Add logic to append the element to the list


# TODO: Modify the dictionary by adding a key-value pair (do not return the dictionary)
def add_key_value_to_dict(d, key, value):
    """
    Modify the dictionary by adding a new key-value pair.
    This function should NOT return anything.

    :param d: The dictionary to be modified
    :param key: The key for the new entry
    :param value: The value for the new entry
    """
    pass  # TODO: Add logic to update the dictionary with the key-value pair


# TODO: Modify the list by changing an element at a specific index (do not return the list)
def change_element_in_list(lst, index, new_value):
    """
    Modify the list by changing the element at the specified index to 'new_value'.
    This function should NOT return anything.

    :param lst: The list to be modified
    :param index: The index of the element to change
    :param new_value: The new value to assign to the element at the specified index
    """
    pass  # TODO: Add logic to modify the list at the specified index


# Unit Test for the Exercise
import unittest


class TestMutableTypesModification(unittest.TestCase):

    def test_add_element_to_list(self):
        lst = [1, 2, 3]
        add_element_to_list(lst, 4)
        self.assertEqual(lst, [1, 2, 3, 4], "Failed to add an element to the list")

    def test_add_key_value_to_dict(self):
        d = {"a": 1, "b": 2}
        add_key_value_to_dict(d, "c", 3)
        self.assertEqual(
            d,
            {"a": 1, "b": 2, "c": 3},
            "Failed to add a key-value pair to the dictionary",
        )

    def test_change_element_in_list(self):
        lst = [1, 2, 3]
        change_element_in_list(lst, 1, 10)
        self.assertEqual(lst, [1, 10, 3], "Failed to change the element in the list")


if __name__ == "__main__":
    unittest.main()
