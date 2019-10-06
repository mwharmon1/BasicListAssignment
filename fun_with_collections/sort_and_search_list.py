"""
Author: Michael Harmon
Date: 10/06/2019
Description: This program will search and sort a list using
the sort_list and search_list functions.
"""


def sort_list(my_list):
    """
    sort a list input by the user
    :param my_list: list input by the user
    """
    pass


def search_list(my_list, number):
    """
    search the list for a given number
    :param my_list:
    :param number:
    :return: index of number in list or -1 if not found it list
    """
    try:
        index_of_number = my_list.index(number)
    except ValueError:
        return -1
    else:
        return index_of_number


if __name__ == '__main__':
    search_list()
    sort_list()
