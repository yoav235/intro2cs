#################################################################
# FILE : temperature.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: gets 4 numbers and checks 3 of them if 2 or more are bigger than the 4th number.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################


def is_vormir_safe(safe_temp, day1_temp, day2_temp, day3_temp):
    three_days_forecast = [day1_temp, day2_temp, day3_temp]
    good_day_counter = 0
    for temp in three_days_forecast:
        if safe_temp < temp:
            good_day_counter += 1
        if good_day_counter > 1:
            return True
    return False

print(is_vormir_safe(7, 5, -2, 11))

