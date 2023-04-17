import math
#################################################################
# FILE : math_print.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: a simple program that prints some math equastions and constants.
# STUDENTS I DISCUSSED THE EXERCISE WITH: yonatan levi.
# WEB PAGES I USED: https://www.w3schools.com/python/ref_math_sin.asp ,
# https://www.google.com/search?client=firefox-b-d&q=basic+math+function+in+python
# NOTES:
#################################################################


# outputs the value of golden ratio
def golden_ratio():
    print((1+math.sqrt(5))/2)


# outputs the value of six in the power of 2
def six_squared():
    print(math.pow(6, 2))


# outputs the value of the hypotenuse of a right triangle with 5 and 12 units vertices
def hypotenuse():
    print(math.sqrt(12*12+5*5))


# outputs the value of pi
def pi():
    print(math.pi)


# outputs the value of e
def e():
    print(math.e)


# outputs the area of a square
def squares_area():
    print(math.pow(1, 2), math.pow(2, 2), math.pow(3, 2), math.pow(4, 2), math.pow(5, 2), math.pow(6, 2), math.pow(7, 2)
          , math.pow(8, 2), math.pow(9, 2), math.pow(10, 2))


if __name__ == "__main__":
    golden_ration()
    six_squared()
    pi()
    e()
    hypotenuse()
    squares_area()
