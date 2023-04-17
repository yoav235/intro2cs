#################################################################
# FILE : largest_to_smallest.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: this file has 2 functions. one function outputs it's smallest and largest values of it's 3 parameters.
# the other function checks the first function works.
# STUDENTS I DISCUSSED THE EXERCISE WITH: yonatan levi.
# WEB PAGES I USED:https://www.programiz.com/python-programming/for-loop
# NOTES:
#################################################################


def largest_and_smallest(avenger1, avenger2, avenger3):
    # putting all the parameters in a list so i can use it in a "for" loop
    list_of_avengers = (avenger1, avenger2, avenger3)
    strongest = avenger1
    weakest = avenger3
    # this loop puts the largest parameter in the "strongest" variable and the smallest parameter in the "weakest"
    # variable.
    for hero in list_of_avengers:
        if hero > strongest:
            strongest = hero
        if hero < weakest:
            weakest = hero
    return strongest, weakest


def check_largest_and_smallest():
    honest_counter = 0
    if str(largest_and_smallest(17, 1, 6)) == "(17, 1)":
        honest_counter += 1
    if str(largest_and_smallest(1, 17, 6)) == "(17, 1)":
        honest_counter += 1
    if str(largest_and_smallest(1, 1, 2)) == "(2, 1)":
        honest_counter += 1
    if str(largest_and_smallest(1.7, 1.5, 6)) == "(6, 1.5)": # it checks if the function can compare floats
        honest_counter += 1
    if str(largest_and_smallest(6, 6, 6)) == "(6, 6)": # it checks that the function can work when all parameters
        # are equal
        honest_counter += 1
    if honest_counter == 5:
        return True
    return False

print(check_largest_and_smallest())



