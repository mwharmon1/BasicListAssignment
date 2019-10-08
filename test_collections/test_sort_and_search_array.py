import unittest
from fun_with_collections import sort_and_search_array as a


class MyTestCase(unittest.TestCase):
    def test_search_list_item_found(self):
        self.assertEqual(a.search_array([8, 6, 'Hi'], 'Hi'), 2)

    def test_search_list_item_not_found(self):
        self.assertEqual(a.search_array([9, 1, 4], 7), -1)


if __name__ == '__main__':
    unittest.main()
