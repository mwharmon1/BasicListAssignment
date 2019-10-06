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
        number = get_input()
        try:
            number = int(number)
        except ValueError:
            print("Numbers Only.")
        else:
            num_list[len(num_list):] = [number]
    return num_list


def get_input():
    """
    this function will prompt user for input
    :return: string input
    """
    number = input("Enter a number: ")
    return number


if __name__ == '__main__':
    print(make_list())
