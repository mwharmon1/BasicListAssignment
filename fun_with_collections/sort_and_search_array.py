"""
Author: Michael Harmon
Date: 10/07/2019
Description: This program will search and sort an array using
the sort_array and search_array functions.
"""
import array as arr


def sort_array(array_to_sort):
    pass


def search_array(array_to_search, my_number):
    try:
        index_of_number = array_to_search.index(my_number)
    except ValueError:
        return -1
    else:
        return index_of_number
    # pass


if __name__ == '__main__':
    my_array = arr.array = [1, 2, 'Test']
    sort_array(my_array)
    print(search_array(my_array, 'Test'))
