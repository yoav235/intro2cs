#################################################################
# FILE : ex3.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex3 2021
# DESCRIPTION: input_list function get a bunch of numbers from the user and returns a list with these numbers and
# their sum. inner_product function gets 2 vectors and calculates the sum of the multiplications of their coordinates.
# sequence_monotonicity function gets a sequence and checks which of the 4 types of sequences it matches.
# monotonicity_inverse outputs an example sequence according to the type or types of sequence the user want.
# primes_for_asafi function - user inputs a number, function outputs the same number of prime numbers.
# sum_of_vectors function calculates the sum of coordinates for the vectors that were input to the function.
# num_of_orthogonal function check how many orthogonals are in the vectors that were input to the function.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: man, i hate descriptions almost as much as i hate notes.
#################################################################


def input_list():
    user_input = input()
    return_list = [0]
    index_in_list = 0
    while user_input != "":
        return_list[index_in_list] = float(user_input)
        index_in_list += 1
        user_input = input()
        return_list.append(0) # i put 0 there because i wanted to fill in the space, it couldve been anything
    return_list[index_in_list] = sum_of_inputs(return_list)
    return return_list


def sum_of_inputs(list_of_inputs):
    total_sum = 0
    for an_input in list_of_inputs:
        total_sum += an_input
    return total_sum
# end part 1


def inner_product(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        return None
    if len(vec_1) == 0 or len(vec_2) == 0:
        return 0
    inner_multiple = 0
    for index in range(len(vec_2)):
        inner_multiple += vec_2[index]*vec_1[index]
    return inner_multiple
# end part 2


def sequence_monotonicity(sequence):
    if len(sequence) == 0 or len(sequence) == 1:
        return [True, True, True, True]
    return [ascending_seq(sequence), really_ascending_seq(sequence), descending_seq(sequence),
            really_descending_seq(sequence)]


def ascending_seq(sequence):
    for index in range(len(sequence)-1):
        if sequence[index] > sequence[index+1]:
            return False
        else:
            continue
    return True


def really_ascending_seq(sequence):
    for index in range(len(sequence)-1):
        if sequence[index] >= sequence[index+1]:
            return False
        else:
            continue
    return True


def descending_seq(sequence):
    for index in range(len(sequence)-1):
        if sequence[index] < sequence[index+1]:
            return False
        else:
            continue
    return True


def really_descending_seq(sequence):
    for index in range(len(sequence)-1):
        if sequence[index] <= sequence[index + 1]:
            return False
        else:
            continue
    return True
# end part 3


def monotonicity_inverse(def_bool):
    if is_seq_illegal(def_bool):
        return None
    if def_bool[0]:
        if def_bool[1]:
            return [1, 2, 3, 4]
        else:
            return [1, 2, 2, 4]
    if def_bool[2]:
        if def_bool[3]:
            return [4, 3, 2, 1]
        else:
            return [4, 3, 3, 1]


def is_seq_illegal(def_bool):
    if (not def_bool[0]) and def_bool[1]:
        return True
    elif def_bool[0] and (def_bool[2] or def_bool[3]):
        return True
    elif (not def_bool[2]) and def_bool[3]:
        return True
    elif def_bool[2] and (def_bool[0] or def_bool[1]):
        return True
    return False
# end part 4


def primes_for_asafi(n):
    prime_counter = 0
    num_in_question = 2
    list_of_prime = []
    while prime_counter < n:
        if is_it_prime(num_in_question):
            list_of_prime.append(num_in_question)
            prime_counter += 1
        num_in_question += 1
    return list_of_prime


def is_it_prime(num):
    for i in range(num, 2, -1):
        divisor = i - 1
        if num % divisor == 0:
            return False
    return True
# end part 5


def sum_of_vectors(vec_lst):
    if len(vec_lst) == 0:
        return None
    if len(vec_lst[0]) == 0:
        return []
    vec_sum_list = []
    for inner_index in range(len(vec_lst[0])):
        cordinate_sum = 0
        for outer_index in range(len(vec_lst)):
            cordinate_sum += vec_lst[outer_index][inner_index]
        vec_sum_list.append(cordinate_sum)
    return vec_sum_list
# end part 6


def num_of_orthogonal(vectors):
    orthogonals = 0
    for the_multiplee in range(len(vectors)-1):
        the_multiplier = the_multiplee + 1
        for the_multiplier in range(1,len(vectors)):
            if inner_product(vectors[the_multiplee], vectors[the_multiplier]) == 0:
                orthogonals += 1
    return orthogonals
# end part 7








