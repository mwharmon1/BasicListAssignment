"""
Author: Michael Harmon
Date: 10/07/2019
Description: This program will search and sort an array using
the sort_array and search_array functions.
"""
import array as arr


def sort_array(array_to_sort):
    # I am not returning an array here since a new array is not created only sorted.
    """
    sort an array that is passed in with no return
    :param array_to_sort: array that is passed into function
    :return: no return
    """
    try:
        array_to_sort.sort()
    except ValueError:
        raise ValueError


def search_array(array_to_search, value):
    """
    search an array that is passed in
    :param array_to_search: the array that is passed in
    :param value: number to be searched for in array
    :return: -1 if not found and index of value if found
    """
    try:
        index_of_number = array_to_search.index(value)
    except ValueError:
        return -1
    else:
        return index_of_number


if __name__ == '__main__':
    my_array = arr.array = [8, 2, 6]
    print(sort_array(my_array))
    print(search_array(my_array, 6))
