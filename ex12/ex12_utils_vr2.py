import copy
#from node import *
from typing import*

SURROND_DICT = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
COORDINATE_TYPE = list[tuple[int, int]]
BOARD_TYPE = list[list[str]]


def is_valid_path(board: BOARD_TYPE, path: COORDINATE_TYPE, words: list[str]) -> Optional[str]:
    if not(is_path_legal(board, path)):
        return None
    word = ""
    for coordinate in path:
        word += board[coordinate[0]][coordinate[1]]
    if word in words:
        return word
    return None


def is_path_legal(board, path: COORDINATE_TYPE) -> bool:
    for index in range(len(path)):
        if path[index][0] >= len(board) or path[index][0] < 0 or path[index][1] >= len(board[0]) or path[index][1] < 0:
            return False
        if index != len(path) - 1:
            if abs(path[index][0] - path[index+1][0]) >= 2 or abs(path[index][1] - path[index+1][1]) >= 2:
                return False
    return True


def board_to_dict(board):
    board_dict = {}
    for y in range(len(board)):
        for x in range(len(board[y])):
            board_dict[(y, x)] = board[y][x]
    return board_dict


def filter_under_n_words(n: int, words):
    filtered_words = []
    for word in words:
        if len(word) >= n:
            filtered_words.append(word.strip().upper())
    return filtered_words


def randomize_first_paths(n: int, board_dict, words):
    all_paths = []
    for coordinate in board_dict.keys():
        all_paths.append([coordinate])
    return path_randomizer(n, all_paths, board_dict, words)


def path_randomizer(n: int, all_paths, board_dict, words, n_counter=1):
    if n_counter == n:
        return all_paths
    new_paths = []
    for path in range(len(all_paths)):
        for move in SURROND_DICT:
            new_coordinate = (all_paths[path][-1][0] + move[0], all_paths[path][-1][1] + move[1])
            if is_coordinate_in_board(new_coordinate) and new_coordinate not in all_paths[path]:
                all_paths[path].append(new_coordinate)
                if is_path_in_words(words, all_paths[path], board_dict):
                    new_paths.append(copy.deepcopy(all_paths[path]))
                all_paths[path].pop()
    return path_randomizer(n, new_paths, board_dict, words, n_counter+1)


def word_builder(board_dict: dict, path: COORDINATE_TYPE):
    word = ""
    for coordinate in path:
        word += board_dict[coordinate]
    return word


def is_path_in_words(words, path, board_dict):
    compared_word = word_builder(board_dict, path)
    for word in words:
        if compared_word in word:
            return True
    return False


def find_length_n_paths(n: int, board: BOARD_TYPE, words: list[str]) -> list[COORDINATE_TYPE]:
    # return randomize_first_paths(n, board_to_dict(board), words)
    coordinate_list = []
    words = filter_under_n_words(n, words)
    # possible_paths = randomize_first_paths(n, board)
    # board_dict = board_to_dict(board)
    # for path in possible_paths:
    #     if word_builder(board_dict, path) in words:
    #         coordinate_list.append(path)
    for word in words:
        word = word.strip()
        word = word.upper()
        for y in range(len(board)):
            for x in range((len(board[y]))):
                if is_cell_in_word(board[y][x], word):
                    path_lst = find_word(word, word, board, (y, x), [(y, x)], [])
                    for path in path_lst:
                        if len(path) == n and path not in coordinate_list and\
                                is_word_legally_in_board(word, board, path):
                            coordinate_list.append(path)
    return coordinate_list


def find_word(word: str, complete_word: str, board: BOARD_TYPE, coordinate: tuple[int, int],
              path_list: Optional[COORDINATE_TYPE], all_path_list) -> Optional[list[COORDINATE_TYPE]]:
    if len(word) == 0:
        return path_list
    length_cell = len(board[coordinate[0]][coordinate[1]])
    new_word = word[length_cell::]
    next_list = next_move(coordinate, new_word, board)
    if next_list == []:
        all_path_list.append(copy.deepcopy(path_list))
        return []
    for cell in next_list:
        if cell in path_list:
            continue
        path_list.append(cell)
        find_word(new_word, complete_word, board, cell, path_list, all_path_list)
        path_list.pop()
    if word == complete_word:
        return all_path_list
    return []


def next_move(coordinate: tuple[int, int], word: str, board: BOARD_TYPE) -> Optional[COORDINATE_TYPE]:
    if len(word) == 0:
        return []
    path_list = []
    for variable in SURROND_DICT:
        new_coordinate = (coordinate[0] + variable[0], coordinate[1] + variable[1])
        if is_coordinate_in_board(new_coordinate) and\
                is_cell_in_word(board[new_coordinate[0]][new_coordinate[1]], word):
            path_list.append(new_coordinate)
    return path_list


def is_coordinate_in_board(coordinate: tuple[int, int]) -> bool:
    return 0 <= coordinate[0] < 4 and 0 <= coordinate[1] < 4


def is_cell_in_word(cell: str, word: str) -> bool:
    if len(word) < len(cell):
        return False
    for idx in range(len(cell)):
        if cell[idx] != word[idx]:
            return False
    return True


def find_length_n_words(n: int, board: BOARD_TYPE, words: list[str]) -> list[COORDINATE_TYPE]:
    words = filter_words(n, words)
    coordinate_list = []
    for word in words:
        for y in range(len(board)):
            for x in range((len(board[y]))):
                if is_cell_in_word(board[y][x], word):
                    path_lisy = find_word(word, word, board, (y, x), [(y,x)])
                    for path in path_lisy:
                        if is_word_legally_in_board(word, board, path) and path not in coordinate_list:
                            coordinate_list.append(path)
    return coordinate_list


def filter_words(n: int, words: list[str]) -> list[str]:
    filtered_words = []
    for word in words:
        word = word.strip().upper()
        if len(word) == n:
            filtered_words.append(word)
    return filtered_words


def is_word_legally_in_board(word: str, board: BOARD_TYPE, path_list: COORDINATE_TYPE) -> bool:
    compared_word = ""
    for coordinate in path_list:
        compared_word += board[coordinate[0]][coordinate[1]]
    return word == compared_word


def max_score_paths(board: BOARD_TYPE, words: list[str]) -> list[COORDINATE_TYPE]:
    max_lst = []
    for word in words:
        for i in range(len(word), 0, -1):
            paths = find_length_n_paths(i, board, [word])
            if paths:
                max_lst.append(paths[0])
                break
    return max_lst
