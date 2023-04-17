#################################################################
# FILE : quadratic_equation.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: calculate the area of a certain shape
# STUDENTS I DISCUSSED THE EXERCISE WITH: or gold
# WEB PAGES I USED:
# NOTES:
#################################################################
import math


def circle_area(r):
    return r*r*math.pi


def rectangle_area(side1, side2):
    return side1*side2


def triangle_area(side):
    (math.sqrt(3)/4)*side*side


def shape_area():
    shape = float(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if shape == 1 or shape == 2 or shape ==3:
        shape_parameter = float(input())
    if shape == 1:
        return circle_area(shape_parameter)
    elif shape == 2:
        shape_parameter2 = float(input())
        return rectangle_area(shape_parameter, shape_parameter2)
    elif shape == 3:
        return triangle_area(shape_parameter)
    else:
        return None

print(str(shape_area()))