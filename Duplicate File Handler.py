# write your code here
import argparse
import os





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


def print_folder_structure(_path):
    for root, dirs, files in os.walk(_path, topdown=False):
        for name in files:
            print(os.path.join(root, name))


# Code
args = read_input()
path = args.root_folder

if nonEmptyFile(path):
    print_folder_structure(path)

