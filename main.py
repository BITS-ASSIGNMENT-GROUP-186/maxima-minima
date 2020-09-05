"""
This module is the entry point of the application and contains method to run and read data from input file
"""
import os
from utils import Utilities


def run():

    input_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'input', 'inputPS4.txt'))
    output_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output', 'outputPS4.txt'))
    input_file = open(input_file_path, 'r')
    output_file = open(output_file_path, 'w')
    utils = Utilities(input_file)
    input_data_list = utils.create_list_from_input_data()
    for data in input_data_list:
        if not data:
            output_file.write("Empty or invalid row entered \n")
            continue
        if len(data) == 1:
            output_file.write("Single element entered : " + str(data[0]) + "\n")
            continue
        distribution_type = utils.get_distribution_type(data)
        maxima_minima = utils.get_maxima_minima(distribution_type)
        output_file.write(f"{distribution_type} {maxima_minima}\n")


if __name__ == "__main__":
    run()
