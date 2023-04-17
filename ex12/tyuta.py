# def find_word(board, word, coordinate, path_list = []):
#     if len(word) == 0:
#         return path_list
#     path_list.append(coordinate)
#     new_word = word.replace(board[coordinate[0]][coordinate[1]], "")
#     for variable in SURROND_DICT:
#         new_coordinate = (coordinate[0] + variable[0], coordinate[1] + variable[1])
#         if is_coordinate_in_board(new_coordinate) and not(new_coordinate in path_list) and \
#                 is_cell_in_word(board[coordinate[0]][coordinate[1]], word):
#             return find_word(board, new_word, new_coordinate, path_list)
#     return []

def find_length_n_paths(n: int, board: BOARD_TYPE, words: list[str]) -> list[COORDINATE_TYPE]:
    coordinate_list = []
    for word in words:
        word = word.strip()
        word = word.upper()
        for y in range(len(board)):
            for x in range((len(board[y]))):
                if is_cell_in_word(board[y][x], word):
                    path_lst = find_word(word, word, board, (y, x), [(y, x)])
                    for path in path_lst:
                        if len(path) == n and path not in coordinate_list and\
                                is_word_legally_in_board(word, board, path):
                            coordinate_list.append(path)
    return coordinate_list


def find_word(word: str, complete_word: str, board: BOARD_TYPE, coordinate: tuple[int, int],
              path_list: Optional[COORDINATE_TYPE], all_path_list=[]) -> Optional[list[COORDINATE_TYPE]]:
    if len(word) == 0:
        return path_list
    length_cell = len(board[coordinate[0]][coordinate[1]])
    new_word = word[length_cell::]
    next_list = next_move(coordinate, new_word, board)
    if next_list == []:
        all_path_list.append(copy.deepcopy(path_list))
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