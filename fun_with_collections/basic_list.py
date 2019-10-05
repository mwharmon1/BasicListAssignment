"""
Author: Michael Harmon
Date: 10/05/2019
Description: This program will ask for user input and display
the input in a list.
"""


def make_list():
    """
    this function will call get_input()
    :return: list
    """
    num_list = []
    tries = 3
    for i in range(tries):
        try:
            number = get_input()
        except ValueError:
            print("Numbers Only")
        else:
            number = int(number)
            num_list[len(num_list):] = [number]
    return num_list
    # pass


def get_input():
    """
    this function will prompt user for input
    :return: string input
    """
    pass


if __name__ == '__main__':
    make_list()
