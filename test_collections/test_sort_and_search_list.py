import unittest
from fun_with_collections import sort_and_search_list as s


class MyTestCase(unittest.TestCase):
    # search_list tests
    def test_search_list_item_found(self):
        self.assertEqual(s.search_list([4, 1, 8], 8), 2)

    def test_search_list_item_not_found(self):
        self.assertEqual(s.search_list([1, 10, 7], 3), -1)

    # sort_list test
    def test_sort_list(self):
        self.assertEqual(s.sort_list([10, 1, 7]), None)

        # since the sort function does not create a new list
        # it only sorts the current list. The return value of
        # sort_list is None. I am not returning a new list





