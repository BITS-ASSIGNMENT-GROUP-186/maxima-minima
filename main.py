"""
This module is the entry point of the application and contains method to run and read data from input file
"""
import os


def run():

    input_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS4.txt'))


if __name__ == "__main__":
    run()
