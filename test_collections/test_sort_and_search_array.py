import unittest
from fun_with_collections import sort_and_search_array as a


class MyTestCase(unittest.TestCase):
    def test_search_array_item_found(self):
        self.assertEqual(a.search_array([8, 6, 'Hi'], 'Hi'), 2)

    def test_search_array_item_not_found(self):
        self.assertEqual(a.search_array([9, 1, 4], 7), -1)

    def test_sort_array(self):
        self.assertEqual(a.sort_array(['Hello', 4, 1]), 2)


if __name__ == '__main__':
    unittest.main()
