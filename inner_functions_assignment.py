"""
Program: inner_functions_assignment.py
Author: Tony Ehlert
Last date modified: 2/15/2023

The purpose of this program is to call a function that contains to inner functions used to calculate the
area and perimeter of a list of measurements for a rectangle or square and return those calculations as a string and
then print the calculations to the console

The input is number(s) put into list representing the length and width
The output is a print-out to the console containing the calculated area and perimeter
"""
def measurements(measurements_list):
    """
    This function uses the numbers contained in a list and calls an inner function to calculate the area
    and calls another inner function to calculate the perimeter, and then returns the calculated area
    and perimeter as a single string value. If more than two numbers are in the list or the list is empty
    the return string indicates that.

    :param measurements_list: list of measurement numbers to be used in calculating the perimeter and area
    :return: string containing the calculated area and perimeter
    """
    def area(measurements_list):
        """
        This method uses the numbers contained in the list to calculate the area and return that value

        :param measurements_list: list of measurement numbers to be used in calculating the perimeter
        :return: number representing the calculated area
        """

        #if statements to determine if one or two numbers are in the list
        if (len(measurements_list) == 1):
            width = measurements_list[0]
            length = measurements_list[0]
        else:
            width = measurements_list[0]
            length = measurements_list[1]

        # creation of variable to hold the calculated area
        calc_area = length * width
        return calc_area

    def perimeter(measurements_list):
        """
        This method uses the numbers contained in the list to calculate the perimeter and return that value

        :param measurements_list: list of measurement numbers to be used in calculating the perimeter
        :return: number representing the calculated perimeter
        """

        # if statements to determine if one or two numbers are in the list
        if (len(measurements_list) == 1):
            width = measurements_list[0]
            length = measurements_list[0]
        else:
            width = measurements_list[0]
            length = measurements_list[1]

        # creation of variable to hold the calculated perimeter
        calc_perimeter = (2 * width) + (2 * length)
        return calc_perimeter

    # if statements to determine if more than two numbers are in the list or if list is empty
    if (len(measurements_list) > 2):
        return "Too Many Numbers in List"
    elif (len(measurements_list) == 0):
        return "No Numbers Were in the List"
    else:
        final_string = ("Perimeter= " + str(perimeter(measurements_list)) + ", Area= " + str(area(measurements_list)))
        return final_string

if __name__ == "__main__" :
    #test for rectangle/two numbers in the list
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)

    # test for square/one number in the list
    square = [3.5]
    result = measurements(square)
    print(result)

    # test for more than two numbers in list
    too_many = [1, 2, 3]
    result = measurements(too_many)
    print(result)

    # test for empty list
    no_num = []
    result = measurements(no_num)
    print(result)