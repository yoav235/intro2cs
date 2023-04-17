#################################################################
# FILE : ex7.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex7 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:https://towardsdatascience.com/type-annotations-in-python-d90990b172dc
# NOTES:
#################################################################


from ex7_helper import *
from typing import *


def pow(base: int, maarich: int, constant: int) -> int:
    if maarich < 2:
        return base
    return pow(int(log_mult(base, constant)), maarich - 1, constant)
#  ----------- supporting function -----------------------------


def mult(x: float, y: int) -> float:
    return _mult_core(0, y, x)


def _mult_core(x: float, y: int, constant: float) -> float:
    if y < 1:
        return x
    return _mult_core(add(x, constant), subtract_1(y), constant)
# ------------------- mult function -------------------------


def is_even(n: int) -> bool:
    if n < 1:
        return True
    return not(is_even(subtract_1(n)))
# ------------------- is even function -----------------------


def log_mult(x: float,y: int) -> float:
    return _log_mult_core(0, y, x)


def _log_mult_core(x: float, y: int, constant:float) -> float:
    if y < 1:
        return x
    x = _log_mult_core(x,divide_by_2(y),constant)
    if is_odd(y):
        return add(add(x,x),constant)
    else:
        return add(x,x)
#--------------------- log_mult function ---------------------


def is_power(b: int, x: int) -> bool:
    return _is_power_core(b, x, b)


def _is_power_core(b: int, x: int, constant: int) -> bool:
    if b == x:
        return True
    elif b > divide_by_2(x):
        return False
    return _is_power_core(int(log_mult(b, constant)), x, constant)
# --------------- is_power function ---------------------------------


def reverse(s: str) -> str:
    return _reverse_core(s, len(s)-1, "")


def _reverse_core(s: str, index: int, output: str) -> str:
    if index < 0:
        return output
    output = append_to_end(output, s[index])
    return _reverse_core(s, index-1, output)
# ----------------- reverse function ----------------------------------


def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> Any:
    if n > 0:
        play_hanoi(Hanoi, subtract_1(n), src, temp, dst)
        Hanoi.move(src, dst)
        play_hanoi(Hanoi, subtract_1(n), temp, dst, src)
    elif n < 0:
        return dst
# ----------------- play hanoi function -------------------------------


def number_of_ones(n: int) -> int:
    if n < 1:
        return 0
    num_1 = _num_of_ones_core(n)
    return int(add(number_of_ones(subtract_1(n)),num_1))


def _num_of_ones_core(n: int) -> int:
    if n < 1:
        return 0
    return_value = _num_of_ones_core(n//10)
    if n%10 == 1:
        return int(add(return_value,1))
    return return_value


# def _num_of_ones_core(n, digits_num):
#     if digits_num <= 2:
#         return 20
#     return add(log_mult(10, _num_of_ones_core(n, digits_num-1)), pow(10,digits_num-1, 10))


# def num_of_digits(n, div=10, counter=1):
#     if n%div == n:
#         return counter
#     return num_of_digits(n, log_mult(div, 10), add(counter,1))
# ---------------------- num_of_ones function --------------------------------------


def compare_2d_lists(l1: list[list[int]], l2: list[list[int]]) -> bool:
    if len(l1) != len(l2):
        return False
    return _compare_rows(l1,l2, 0)


def _compare_rows(l1: list[list[int]], l2: list[list[int]], row_index: int) -> bool:
    if row_index == len(l1):
        return True
    if len(l1[row_index]) != len(l2[row_index]):
        return False
    if _compare_element(l1[row_index], l2[row_index], 0):
        return _compare_rows(l1,l2,int(add(row_index,1)))
    else:
        return False



def _compare_element(row_l1: list[int], row_l2: list[int], element_index: int) -> bool:
    if element_index == len(row_l2):
        return True
    if len(row_l1) != len(row_l2):
        return False
    if row_l1[element_index] == row_l2[element_index]:
        return _compare_element(row_l1, row_l2, int(add(element_index,1)))
    else:
        return False
# ------------------------------- compare_2d_lists function ------------------------


def magic_list(n: int) -> list[Any]:
    return _magic_list_core(n, [])


def _magic_list_core(n: int, lst: list[Any]) -> list[Any]:
    if n == 0:
        return lst
    lst.append(lst[:])
    return _magic_list_core(subtract_1(n), lst)

#
#
#
# def somting()
