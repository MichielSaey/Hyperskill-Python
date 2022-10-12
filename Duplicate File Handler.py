# write your code here
import argparse
import os
from typing import Dict


def nonEmptyFile(path):
    if path is None or path == "":
        print("Directory is not specified")
        return False
        # raise argparse.ArgumentTypeError('Directory is not specified')
    elif not os.path.exists(path):
        print("Given path does not exist.")
        return False
        # raise argparse.ArgumentTypeError("Directory does not exist.")

    return True


def read_input():
    # print("Read file:")
    parser = argparse.ArgumentParser(
        description='This program gives a list of files and folders for a specific path'
    )

    parser.add_argument(
        "root_folder",
        nargs="?",
        default=None,
        help="Root folder for where to search for folders and files",

    )

    args = parser.parse_args()

    return args


def create_dictionary_folder_structure(_path):
    dictionary: Dict[int, list] = dict()
    for root, dirs, files in os.walk(_path, topdown=False):
        for name in files:
            file = os.path.join(root, name)
            size = os.stat(file).st_size

            if size in dictionary:
                file_list = dictionary[size]
                file_list.append(file)
                dictionary.update({size: file_list})
            else:
                dictionary.update({size: [file]})

    return dictionary


def read_file_type():
    file_type = None
    while file_type is None:
        print("Enter file format:")
        file_type = input()
    return file_type


def read_sort():
    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")

    selection = 0
    while True:
        print("Enter a sorting option:")
        selection = int(input())
        if selection in [1, 2]:
            return True if selection == 1 else False
        else:
            print("/nWrong Option:/n")


def print_dictionary(dictionary):
    for key, values in dictionary.items():
        print(f'{key} bytes')
        for file in values:
            print(file)


def filter_dictionary(dictionary, file_type):
    new_dictionary: Dict[int, list] = dict()
    for size, files in dictionary.items():

        new_files = [file for file in files if file.endswith(file_type)]

        if new_files:
            new_dictionary.update({size: new_files})

    return new_dictionary


def sort_dictionary(dictionary, sort):
    order = sorted(dictionary)
    new_dictionary: Dict[int, list] = dict()

    if sort:
        order.reverse()

    for i in order:
        files = dictionary[i]
        new_dictionary.update({i: files})

    return new_dictionary


def run():
    args = read_input()
    path = args.root_folder

    if nonEmptyFile(path):
        dictionary = create_dictionary_folder_structure(path)

        file_type = read_file_type()
        dictionary = filter_dictionary(dictionary, file_type)

        sort = read_sort()
        dictionary = sort_dictionary(dictionary, sort)
        print_dictionary(dictionary)


# Code
if __name__ == '__main__':
    run()

