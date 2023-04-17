import copy
from typing import*

from typing import List, Tuple, Dict


def board_coordiantes():
    """
    this function returns a list with tuples of all board coordinates in form of (y,x)
    where y is the row index and accordingly x is the column index.
    :return: list of all board coordinates.
    """
    coordinate_list = []
    for y in range(4):
        for x in range(4):
            coordinate_list.append((y, x))
    return coordinate_list


SURROND_DICT = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
COORDINATES = board_coordiantes()


def is_valid_path(board, path, words: List[str]) -> Optional[str]:
    """
    this function checks whether a path it receives is for word contained in the words list, and
     whether the path to it is legal
    :param board: 2D list of all 16 characters of the board.
    :param path: list of tuples of possible path to a word.
    :param words: list of all legal words.
    :return: the word if all conditions met, None otherwise.
    """
    if not(is_path_legal(board, path)):
        return None
    word = ""
    for coordinate in path:
        word += board[coordinate[0]][coordinate[1]]
    if word in words:
        return word
    return None


def is_path_legal(board, path) -> bool:
    """
    this is sub function for helping is_valid_path to determine whether the path is legal by the number
     of steps allowed.
    :param board: 2D list of all 16 characters of the board.
    :param path: list of tuples of possible path to a word.
    :return: True if all the steps in the path are legal, False otherwise.
    """
    for index in range(len(path)):
        if path[index][0] >= len(board) or path[index][0] < 0 or path[index][1] >= len(board[0]) or path[index][1] < 0:
            return False
        if index != len(path) - 1:
            if abs(path[index][0] - path[index+1][0]) >= 2 or abs(path[index][1] - path[index+1][1]) >= 2:
                return False
    return True


def find_max_possible_length(n: int, board) -> int:
    """
    this function helps to set the upper limit for word length, to reduce the running time of find_length_n_paths.
    :param n: lower limit of word length.
    :param board: 2D list of all 16 characters of the board.
    :return: an integer of upper limit for path length to be found.
    """
    m = n
    for x in board:
        for cell in x:
            if len(cell) > 1:
                m += (len(cell) - 1)
    return m


def find_length_n_paths(n: int, board, words: List[str]):
    """
    this function finds all the paths of legal words in the board, in length of n.
    :param n: lower limit of word length.
    :param board: 2D list of all 16 characters of the board.
    :param words: list of all legal words allowed in the board.
    :return: list of all possible paths in length n of all words in the list.
    """
    coordinate_list = []
    words = filter_impossible_words(n, find_max_possible_length(n, board), words)
    for word in words:
        for y, x in COORDINATES:
            if is_cell_in_word(board[y][x], word):
                path_lst = find_word(word, word, board, (y, x), [(y, x)], [])
                for path in path_lst:
                    if len(path) == n and path not in coordinate_list and\
                            is_word_legally_in_board(word, board, path):
                        coordinate_list.append(path)
    return coordinate_list


def filter_impossible_words(n: int, m: int, words) :
    """
    this function alternate a dictionary with all words up for find_length_n_paths, to reduce its running time.
    :param n: a lower limit of words length.
    :param m: an upper limit of words length.
    :param words: list of all legal words to be found in the board.
    :return: a dictionary with all the relevant words to be found.
    """
    filtered_words = {}
    for word in words:
        if m >= len(word) >= n:
            filtered_words[word.strip().upper()] = ""
    return filtered_words


def find_word(word: str, complete_word: str, board, coordinate,
              path_list, all_path_list):
    """
    this function used for finding all possible paths in the board for given word. uses a backtracking methods.
    :param word: word to be found on the board.
    :param complete_word: string that writen with the function running to compare the word, whether the process ended.
    :param board: 2D list of all 16 characters of the board.
    :param coordinate: tuple with the first appearance of the word on the board.
    :param path_list: list of current path coordinates.
    :param all_path_list: list of all possible paths to the word.
    :return: list of all possible paths to the word.
    """
    if len(word) == 0:
        return path_list
    length_cell = len(board[coordinate[0]][coordinate[1]])
    new_word = word[length_cell::]
    next_list = next_move(coordinate, new_word, board)
    if not next_list:
        all_path_list.append(copy.deepcopy(path_list))
        return all_path_list
    for cell in next_list:
        if cell in path_list:
            continue
        path_list.append(cell)
        find_word(new_word, complete_word, board, cell, path_list, all_path_list)
        path_list.pop()
    if word == complete_word:
        return all_path_list
    return []


def next_move(coordinate, word: str, board):
    """
    this function helps find_word function to find the next move given a single path list.
    :param coordinate: tuple with the last coordinate in the current path.
    :param word: the next part of the word to be found.
    :param board: 2D list of all 16 characters of the board.
    :return: path list with added next coordinate.
    """
    if len(word) == 0:
        return []
    path_list = []
    for variable in SURROND_DICT:
        new_coordinate = (coordinate[0] + variable[0], coordinate[1] + variable[1])
        if is_coordinate_in_board(new_coordinate) and\
                is_cell_in_word(board[new_coordinate[0]][new_coordinate[1]], word):
            path_list.append(new_coordinate)
    return path_list


def is_coordinate_in_board(coordinate):
    """
    this function helps next_move to determine whether it's in the board or not.
    :param coordinate: tuple with coordinate to be checked.
    :return: True if it's the board, False if not.
    """
    return 0 <= coordinate[0] < 4 and 0 <= coordinate[1] < 4


def is_cell_in_word(cell: str, word: str) -> bool:
    """
    checks if the charcaters in the cell of the board are equals to the first letters of a given string.
    :param cell: the letters in the cell
    :param word: a given string
    :return: True if they are equal, False otherwise.
    """
    if len(word) < len(cell):
        return False
    for idx in range(len(cell)):
        if cell[idx] != word[idx]:
            return False
    return True


def find_length_n_words(n: int, board, words: List[str]):
    """
    finds every path for every word in the length of n characters in the given dictionary.
    :param n: the length of the word that we are going to find its paths.
    :param board: the board of the game.
    :param words: the given list of words for the game
    :return: a list of lists of coordinates, or a list of paths.
    """
    words = filter_words(n, words)
    coordinate_list = []
    for word in words:
        # if len(word) == n:
        for y,x in COORDINATES:
            if is_cell_in_word(board[y][x], word):
                path_lisy = find_word(word, word, board, (y, x), [(y,x)], [])
                for path in path_lisy:
                    if is_word_legally_in_board(word, board, path) and path not in coordinate_list:
                            coordinate_list.append(path)
    return coordinate_list


def filter_words(n: int, words: List[str]):
    """
    find_length_n_words sub-function. filters from the dictionary all words that aren't the length of n.
    :param n: the legal length of the word
    :param words: the given list of words for the game
    :return: a dictionary of string in the length of n
    """
    filtered_words = {}
    for word in words:
        if len(word) == n:
            filtered_words[word.strip().upper()] = ""
    return filtered_words


def is_word_legally_in_board(word: str, board, path_list) -> bool:
    """
    checks if the paths builds a word on the board
    :param word: the word that the path needs to build
    :param board: the game board
    :param path_list: a list of coordinates, in other words - a path.
    :return: True if the path builds the word, False otherwise.
    """
    compared_word = ""
    for coordinate in path_list:
        compared_word += board[coordinate[0]][coordinate[1]]
    return word == compared_word


def max_score_paths(board, words: List[str]):
    """
    returns a list of the maximum length of a path for each word in the game list of words.
    :param board: game board
    :param words: list of words for the game
    :return: a lsit of lists of coordinates, in other words a list of paths.
    """
    max_lst = []
    for word in words:
        # finds all the paths creates the word
        paths = find_length_n_words(len(word), board, [word])
        if paths:
            max_lst.append(find_max_path(paths, word))
    return max_lst


def find_max_path(path_list, word):
    """
    finds the longest path for a given word in the list of words of the game.
    :param path_list: the paths for the given word
    :param word: the given word
    :return: one path, which is the longest.
    """
    max_path = []
    for path in path_list:
        if len(path) == len(word):
            return path
        if len(path) > len(max_path):
            max_path = path
    return max_path


