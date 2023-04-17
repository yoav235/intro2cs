#################################################################
# FILE : hangman.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex4 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:https://www.decalage.info/en/python/print_list,
# https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/,
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/,
# https://careerkarma.com/blog/python-count/
# NOTES:
#################################################################
import hangman_helper


def main():
    word_list = hangman_helper.load_words()
    player_points = hangman_helper.POINTS_INITIAL
    while hangman_helper.play_again("would you like to play a game?"):
        player_points = run_single_game(word_list, player_points)
        if player_points == 0:
            break


def update_word_pattern(word, pattern, letter):
    pattern_list = list(pattern)
    index = 0
    for char in word:
        if char == letter:
            pattern_list[index] = letter
        index += 1
    return ''.join(pattern_list)


def run_single_game(word_list, score):
    player_points = score
    word = hangman_helper.get_random_word(word_list)
    pattern = conceal_word(word)
    wrong_guesses_list = []
    do_it_again = True
    while do_it_again:
        hangman_helper.display_state(pattern, wrong_guesses_list, player_points, "don't keep us hanging ;)")
        user_input = hangman_helper.get_input()
        # if a letter is chosen
        if user_input[0] == hangman_helper.LETTER:
            if not (is_input_legal(user_input[1], wrong_guesses_list, pattern)):
                player_points += 1
            else:
                pattern, player_points, wrong_guesses_list  = good_letter(word, player_points, user_input[1],
                                                                          wrong_guesses_list, pattern)
            player_points -= 1
        # if a word is chosen | iilegal inputs prints shit you don't want, FIX IT
        elif user_input[0] == hangman_helper.WORD:
            added_points = 0
            for letter in user_input[1]:
                pattern, added_points, wrong_guesses_list = good_letter(word, added_points, letter,
                                                                            wrong_guesses_list, pattern)
            player_points -= 1
            player_points += added_points*((added_points+1)//2)
        #if the player wants a hint
        if user_input[0] == hangman_helper.HINT:
            player_points -= 1
            hint_list = filter_word_list(word_list, pattern, wrong_guesses_list)
            print(hint_list)
        #ENDGAME
        if pattern == word:
            hangman_helper.display_state(pattern, wrong_guesses_list, player_points, "congrats")
            do_it_again = False
        elif player_points < 1:
            hangman_helper.display_state(pattern, wrong_guesses_list, player_points, "INCONCEIVABLE!")
            do_it_again = False
    return player_points


def filter_word_list(words, pattern, wrong_guesses_lst): # keep working on it
    hint_lst = []
    for string in words:
        if len(string) == len(pattern):
            if char_filter(string, pattern):
                if not is_word_wrong(string, wrong_guesses_lst):
                    hint_lst.append(string)
    return hint_lst


# functions to make the code more readable UwU
def is_input_legal(user_input, wrong_guesses_list, pattern):
    if not (user_input.islower()) or len(user_input) != 1:
        print("what are you DOING?! get a lowercase english letter in there!")
        return False
    elif repeated_input(wrong_guesses_list, pattern, user_input):
        print("you already used that.")
        return False
    return True


def good_letter(word, player_points, user_input, wrong_guesses_list, pattern):
    appearences_in_word = word.count(user_input)
    if appearences_in_word == 0 or not(is_input_legal(user_input,wrong_guesses_list,pattern)):
        wrong_guesses_list.append(user_input)
    elif appearences_in_word > 0:
        new_pattern = update_word_pattern(word, pattern, user_input)
        player_points += (appearences_in_word * (appearences_in_word + 1) // 2)
        return new_pattern, player_points, wrong_guesses_list
    return pattern, player_points, wrong_guesses_list


def repeated_input(wrong_lst, pattern, user_input): # checks if you already use that input
    if pattern.count(user_input) > 0:
        return True
    for value in wrong_lst:
        if user_input == value:
            return True
    return False


def conceal_word(word): # replace all characters in given string with '_'.
    concealed_word = word
    for char in word:
        concealed_word = concealed_word.replace(char, '_')
    return concealed_word


def char_filter(word, pattern):
    for index in range(len(pattern)):
        if word[index] == pattern[index]:
            return True
    return False


def is_word_wrong(string, wrong_guesses_list):
    for letter in wrong_guesses_list:
        if string.count(letter) > 0:
            return True
    return False




main()



