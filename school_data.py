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

    # get the boolean mask which holds True for the specific school code
    mask = enrol_data[:, :, 1:2] == school_code

    # spread the mask over all columns
    mask = mask.repeat(5).reshape(8, 20, 5)

    # filter the enrol data based on the mask, ie, choosing only particular school code
    enrol_data_school = enrol_data[mask].reshape(8, 1, 5)

    # again filter only the data points, ie, grade information, by creating a view
    enrol_data_school_grade = enrol_data_school[:, :, 2:5]


    print("Mean enrolment for Grade 10: {0}".format(np.mean(enrol_data_school_grade, axis=0)[0, 0]))
    print("Mean enrolment for Grade 11: {0}".format(np.mean(enrol_data_school_grade, axis=0)[0, 1]))
    print("Mean enrolment for Grade 12: {0}".format(np.mean(enrol_data_school_grade, axis=0)[0, 2]))
    print("Highest enrolment for a single grade: {0}".format(np.max(enrol_data_school_grade)))
    print("Lowest enrolment for a single grade: {0}".format(np.min(enrol_data_school_grade)))

    for i, x in enumerate(enrol_data_school[:, :, 0]):
        print("Total enrolment for {0}: {1}".format(x[0], np.sum(enrol_data_school[i, :, 2:5])))


    # get the boolean mask which holds True for if the enrolment is greater than 500 in any grade for the particular school
    enrol_data_school_grade_over_500 = enrol_data_school_grade > 500

    if enrol_data_school_grade[enrol_data_school_grade_over_500].size == 0:
        print("No enrolments over 500.")

    else:
        print("For all enrolments over 500, the median value was: {0}".format(np.median(enrol_data_school_grade[enrol_data_school_grade_over_500])))


    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    enrol_data_grade = enrol_data[:, :, 2:5]

    print("Mean enrolment in 2013: {0}".format(np.mean(enrol_data_grade[0, :, :])))
    print("Mean enrolment in 2020: {0}".format(np.mean(enrol_data_grade[7, :, :])))
    print("Total graduating class of 2020: {0}".format(np.sum(enrol_data_grade[7, :, 2])))
    print("Highest enrolment for a single grade: {0}".format(np.max(enrol_data_grade[:, :, :])))
    print("Lowest enrollment for a single grade: {0}".format(np.min(enrol_data_grade[:, :, :])))



if __name__ == '__main__':
    main()

