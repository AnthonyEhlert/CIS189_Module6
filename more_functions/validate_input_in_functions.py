"""
Program: validate_input_in_functions.py
Author: Tony Ehlert
Last date modified: 2/15/2023

The purpose of this program is take in a test name and score and call a function to validate the input
and return default values if the input validation fails

The input is a string value representing a test name and an integer value representing a test score

The output is a string value being printed to the console containing the test name and the score
if it was valid and invalid score if it was not valid
"""


def score_input(test_name, test_score=-1, invalid_message="Invalid test score!"):
    """
    Checks the test score to ensure it is in the proper range and that a string was not entered
    or float was not entered

    :param test_name: String value representing name of test
    :param test_score: optional value representing test score (default = -1)
    :param invalid_message: optional string value denoting an invalid input
    :return: string containing the test name and score if valid or invalid_message if invalid
    """

    # creation of base string variable to be returned
    return_string = f"{test_name}: {test_score}"

    # try/except block for possible string input for test_score argument
    try:
        # cast test score to float to ensure input was a number
        test_score_as_float = float(test_score)

        # check number to ensure it is between 0-100
        if (test_score_as_float < 0) or (test_score_as_float > 100):
            return_string = (f"{test_name}: {invalid_message}")
            return return_string
        return return_string
    except ValueError:
        invalid_message = "ValueError encountered!"
        return_string = f"{test_name}: {invalid_message}"
        return return_string


if __name__ == '__main__':
    display_string_good = score_input("Test 1", 70.5)
    print(display_string_good)

    display_string_below_range = score_input("Test 2", -1)
    print(display_string_below_range)

    display_string_above_range = score_input("Test 3", 100.01)
    print(display_string_above_range)

    display_string_non_num = score_input("Test 4", "One Hundred")
    print(display_string_non_num)

    display_string_zero = score_input("Test 5", 0)
    print(display_string_zero)

    display_string_100 = score_input("test 6", 100)
    print(display_string_100)

    display_string_invalid = score_input("Test 7", 101, "Custom Invalid Message for score of 101")
    print(display_string_invalid)



