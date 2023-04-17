import math
#################################################################
# FILE : quadratic_equation.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: solves second degree equations
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################


def quadratic_equation (a, b, c):
    # if b^2 is smaller than 4ac then there are no solutions to the equation.
    if b*b < 4*a*c:
        return None, None
    x1 = (-b-(math.sqrt(b*b - 4*a*c)))/(2*a)
    x2 = (-b+(math.sqrt(b*b - 4*a*c)))/(2*a)
    if x1 == x2:
        return x1, None
    else:
        return x1, x2


def quadratic_equation_user_input():
    parameter_list = input("Insert coefficients a, b, and c: ").split()
    a = float(parameter_list[0])
    b = float(parameter_list[1])
    c = float(parameter_list[2])
    if a == 0:
        print("The parameter 'a' may not equal 0")
        return
    x1, x2 = quadratic_equation(a, b, c)
    if(x1 == None):
        print("The equation has no solutions")
    elif (x2 == None):
        print("The equation has 1 solution: " + str(x1))
    else:
        print("The equation has 2 solutions: " + str(x1) + " and " + str(x2))


