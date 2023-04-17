#################################################################
# FILE : largest_and_smallest.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: there are 2 function: calculate_mathematical_expression and calculate_from_string.
# calculate_mathematical_expression produce an expression using 2 int\float and 1 str parameters and calculates it.
# calculate_from_string produce an expression using 1 str parameter and calculates it.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:https://docs.python.org/3.4/library/stdtypes.html#str.split
# NOTES:
#################################################################


def calculate_mathematical_expression(number1, number2, operator):
    if operator == '+':
        return number1+number2
    elif operator == '-':
        return number1-number2
    elif operator == '*':
        return number1*number2
    # you can't divide by zero so if number2 is zero it needs to skip this condition
    elif operator == ':' and number2 != 0:
        return number1/number2
    else:
        return None


def calculate_from_string(math_experssion):
    expression = math_experssion.split()
    return calculate_mathematical_expression(float(expression[0]), float(expression[2]), expression[1])


print(str(calculate_from_string("1 + 2")))
