import unittest
from fun_with_collections import sort_and_search_list as s


class MyTestCase(unittest.TestCase):
    def test_search_list_item_found(self):
        self.assertEqual(s.search_list([4, 1, 8], 8), 2)

    def test_search_list_item_not_found(self):
        self.assertEqual(s.search_list([1, 10, 7], 3), -1)





