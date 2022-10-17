# write your code here
# write your code here
import argparse
import os
from typing import Dict
from hashlib import md5


def non_empty_file(path):
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
    print("\nSize sorting options:")
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
        print(f'\n{key} bytes')
        for file in values:
            print(file)


def print_hash_dictionary(dictionary):
    idx = 1
    for key, values in dictionary.items():
        print(f'{key} bytes')

        for hash_key, files in values.items():
            print(f'Hash: {hash_key}')

            for file in files:
                print(f'{idx}. {file}')
                idx += 1
        print("")


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


def duplicates_finder(dictionary):

    duplicates_dictionary: Dict[int, Dict[str, list]] = dict()

    for key, values in dictionary.items():
        found_hashes_with_files: Dict[str, list] = dict()
        for value in values:
            hex_m = ""

            with open(value, 'rb') as f1:
                m = md5()
                m.update(f1.read())
                hex_m = m.hexdigest()

            if hex_m in found_hashes_with_files.keys():
                updated_list = found_hashes_with_files.get(hex_m)
                updated_list.append(value)
                found_hashes_with_files.update({hex_m: updated_list})
            else:
                found_hashes_with_files.update({hex_m: [value]})

        duplicates_hashes_with_files = {
            _key: _value for (_key, _value) in found_hashes_with_files.items()
            if len(_value) > 1
        }

        duplicates_dictionary.update({
            key: duplicates_hashes_with_files
        })

    print_hash_dictionary(duplicates_dictionary)


def run():
    args = read_input()
    path = args.root_folder

    if non_empty_file(path):
        dictionary = create_dictionary_folder_structure(path)

        file_type = read_file_type()
        dictionary = filter_dictionary(dictionary, file_type)

        sort = read_sort()
        dictionary = sort_dictionary(dictionary, sort)
        print_dictionary(dictionary)

        print('\nCheck for duplicates?')
        answer = input().strip()
        if answer == 'yes':
            print('')
            duplicates_finder(dictionary)


# Code
if __name__ == '__main__':
    run()
