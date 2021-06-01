import numpy as np
import data_help

# school_data.py
# Bhavyai Gupta
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc.
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


def main():
    print("ENSF 592 School Enrollment Statistics")

    # Print Stage 1 requirements here
    enrol_data, enrol_dict = data_help.load_data()
    print("Shape of full data array:", enrol_data.shape)
    print("Dimensions of full data array:", enrol_data.ndim)

    # Prompt for user input
    while(True):
        user_choice = input("Please enter the high school name or school code: ")
        school_code = enrol_dict.get(user_choice)

        try:
            if school_code is None:
                raise ValueError("You must enter a valid school name or code.")

            else:
                break

        except ValueError as e:
            print(e)


    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    print("School Name: {0}, School Code: {1}".format(enrol_dict.get(school_code), school_code))

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

if __name__ == '__main__':
    main()

