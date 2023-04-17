import copy
from typing import List, Tuple, Set, Optional

# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    """

    :param picture: the board
    :param row: row index in the board
    :param col: column index in the board
    :return: maximum number of white cells that can be seen from the given cell
    """
    if picture[row][col] == 0:
        return 0
    return cell_drive_max(picture, col, row)


def cell_drive_max(picture, cell_x, cell_y):
    """
    :param picture: the board
    :param cell_x: column index of the cell
    :param cell_y: row index of the cell
    :return: maximum number of white cells that can be seen from the given cell
    """
    return 1+cell_drive_forward_max(picture[cell_y], cell_x)+cell_drive_backward_max(picture[cell_y], cell_x)+\
           cell_drive_downward_max(picture, cell_y, cell_x)+cell_drive_upwards_max(picture,cell_y, cell_x)


def cell_drive_forward_max(picture_row, cell_x):
    """
    :param picture_row: a row from the baord
    :param cell_x: column index in the row
    :return: maximum number of white cells that can be seen in front of the given cell
    """
    counter = 0
    for idx in range(cell_x+1, len(picture_row)):
        if picture_row[idx] == 0:
            return counter
        counter += 1
    return counter


def cell_drive_backward_max(picture_row, cell_x):
    """
    :param picture_row: a row from the board
    :param cell_x: column index in the board
    :return: maximum number of white cells that can be seen from the back of the given cell
    """
    counter = 0
    for idx in range(cell_x-1, -1, -1):
        if picture_row[idx] == 0:
            return counter
        counter += 1
    return counter


def cell_drive_upwards_max(picture, cell_y, cell_x):
    """
    :param picture: the board
    :param cell_y: board row index
    :param cell_x: board column index
    :return: maximum number of cells that can be seen from the top of the cell
    """
    counter = 0
    for idx in range(cell_y-1, -1, -1):
        if picture[idx][cell_x] == 0:
            return counter
        counter += 1
    return counter


def cell_drive_downward_max(picture, cell_y, cell_x):
    """
    :param picture: the board
    :param cell_y: board row index
    :param cell_x: board column index
    :return: maximum number of white that can be seen down form the given cell
    """
    counter = 0
    for idx in range(cell_y+1, len(picture)):
        if picture[idx][cell_x] == 0:
            return counter
        counter += 1
    return counter
# -------------------------- maximum cells ----------------------------

def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    """
    :param picture: the board
    :param row: board row index
    :param col: board column index
    :return: minimum white cells that can be seen from the given cell
    """
    if picture[row][col] == 0 or picture[row][col] == -1:
        return 0
    return cell_drive_min(picture, col, row)


def cell_drive_min(picture, cell_x, cell_y):
    """
    :param picture: the board
    :param cell_x: board column index
    :param cell_y: board row index
    :return: minimum white cells that can be seen from the given cell
    """
    return 1+cell_drive_backward_min(picture[cell_y],cell_x)+cell_drive_forward_min(picture[cell_y],cell_x)+\
           cell_drive_downward_min(picture,cell_y,cell_x)+cell_drive_upwards_min(picture,cell_y,cell_x)


def cell_drive_forward_min(picture_row, cell_x):
    """
    :param picture_row: a row from the baord
    :param cell_x: column index in the row
    :return: minimum number of white cells that can be seen in front of the given cell
        """
    counter = 0
    for idx in range(cell_x + 1, len(picture_row)):
        if picture_row[idx] == 0 or picture_row[idx] == -1:
            return counter
        counter += 1
    return counter


def cell_drive_backward_min(picture_row, cell_x):
    """
    :param picture_row: a row from the board
    :param cell_x: column index in the board
    :return: minimum number of white cells that can be seen from the back of the given cell
    """
    counter = 0
    for idx in range(cell_x-1, -1, -1):
        if picture_row[idx] == 0 or picture_row[idx] == -1:
            return counter
        counter += 1
    return counter


def cell_drive_upwards_min(picture, cell_y, cell_x):
    """
    :param picture: the board
    :param cell_y: board row index
    :param cell_x: board column index
    :return: maximum number of cells that can be seen from the top of the cell
    """
    counter = 0
    for idx in range(cell_y-1, -1, -1):
        if picture[idx][cell_x] == 0 or picture[idx][cell_x] == -1:
            return counter
        counter += 1
    return counter


def cell_drive_downward_min(picture, cell_y, cell_x):
    """
    :param picture: the board
    :param cell_y: board row index
    :param cell_x: board column index
    :return: maximum number of white that can be seen down form the given cell
    """
    counter = 0
    for idx in range(cell_y+1, len(picture)):
        if picture[idx][cell_x] == 0 or picture[idx][cell_x] == -1:
            return counter
        counter += 1
    return counter
# -------------------------------- minimum cells -------------------------------------

# ----------------------------- phase 1 ----------------------------------------------


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    """
    :param picture: the board
    :param constraints_set: what are the number of cells that can been seen from a certain cells
    :return: 1 if all of the conditions of the constraint_set is met, 2 if some are met or unknown and 0 if at least one
     condition is breached.
    """
    exist = 0
    for coordinate in constraints_set:
        if check_for_minus_1(coordinate[1], coordinate[0], picture):
            if coordinate[2] < min_seen_cells(picture, coordinate[0], coordinate[1]) or coordinate[2] > max_seen_cells(
                                                                                picture, coordinate[0], coordinate[1]):
                return 0
        else:
            if coordinate[2] != max_seen_cells(picture, coordinate[0], coordinate[1]):
                return 0
            else:
                exist += 1
    if exist == len(constraints_set):
        return 1
    return 2


def check_for_minus_1(cell_x, cell_y, picture):
    """
    :param cell_x: board column index
    :param cell_y: board row index
    :param picture: the board
    :return: True if there's an undefined cells around the given cell
    """
    for element in picture[cell_y]:
        if element == -1:
            return True
    for column_index in range(len(picture)):
        if picture[column_index][cell_x] == -1:
            return True
    return False
# -------------------------------- phase 2 -----------------------------------


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    """
    :param constraints_set: a set of constriants for the board
    :param n: how many rows in board
    :param m: how many columns in board
    :return: a board that validates all f the constraints
    """
    picture = build_picture(n, m, constraints_set)
    constraints_set_copy = set(constraints_set)
    return _solve_puzzle_core(constraints_set_copy, picture, 1, n, m)


def _solve_puzzle_core(constraints_set, picture, stoper, n, m):
    """
    :param constraints_set: same as the shell function
    :param picture: same as the shell function
    :param stoper: when it reaches a certain value it stops the recursion
    :param n: same the shell function
    :param m: same as the shell function
    :return: same as the shell function
    """
    if check_constraints(picture, constraints_set) == 1:
        return copy.deepcopy(picture)
    if stoper >= n*m:
        return picture
    if check_constraints(picture, constraints_set) == 0:
        return
    row, col = stoper//m, stoper%m - 1
    if picture[row][col] != -1:
        _solve_puzzle_core(constraints_set, picture, stoper + 1, n, m)
    for i in range(2):
        picture[row][col] = i
        _solve_puzzle_core(constraints_set, picture, stoper + 1, n, m)
        if check_constraints(picture, constraints_set) == 1:
            return picture
    picture[row][col] = -1










# def zeroing(n):
#     lst = []
#     for i in range(n):
#         lst.append(-1)
#     return lst


def build_picture(rows, columns, constraints_set):
    """
    builds a board
    :param rows: how many rows in the board
    :param columns: how many columns in the board
    :param constraints_set: a set of constraints (duh)
    :return: a board that filled with -1, if they have a constraint puts 0 or 1 accordingly
    """
    picture = []
    for i in range(rows):
        picture.append([])
        for j in range(columns):
            picture[i].append(-1)
    for tuple in constraints_set:
        if tuple[2] == 0:
            picture[tuple[0]][tuple[1]] = 0
        elif tuple[2] >= 1:
            picture[tuple[0]][tuple[1]] = 1
    return picture


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    """
    :param constraints_set:
    :param n:
    :param m:
    :return:
    """
    if len(constraints_set) == 0:
        return (n*m)**2
    num_of_solutions = 0
    picture = build_picture(n,m,constraints_set)
    return _how_many_solutions_core(constraints_set, picture, 0, n, m, num_of_solutions)


def _how_many_solutions_core(constraints_set, picture, stoper, n, m, x):
    if stoper >= n * m:
        return x
    row, col = stoper // m, stoper % m - 1
    if picture[row][col] != -1:
        _how_many_solutions_core(constraints_set, picture, stoper + 1, n, m,x)
    for i in range(2):
        picture[row][col] = i
        if check_constraints(picture, constraints_set) == 0:
            pass
        elif check_constraints(picture, constraints_set) == 1:
            x += 1
        x = _how_many_solutions_core(constraints_set, picture, stoper + 1, n, m, x)
    picture[row][col] = -1
    return x

def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...







# def _solve_puzzle_helper(constraints_set: Set[Constraint], picture):
#
#     # Stop condition
#     if(len(constraints_set) == 0):
#         return True
#     else:
#         current_constraint = constraints_set.pop()
#         if (check_constraints(picture, current_constraint)== 0):
#              return False
#         elif (check_constraints(picture, current_constraint)== 1):
#             return True
#         else:
#             all_possible_pictures = generate_possible_pictures(current_constraint, picture)
#             for current_picture in all_possible_pictures:
#                 if(_solve_puzzle_helper(constraints_set, current_picture)):
#                     picture = current_picture
#                     return True
#             return False
#
#
# def generate_possible_pictures(constraints, picture, column, row):
#     all_pictures = []
#     for constr in constraints:
#         pass
#
#
# # drivers
# def color_upwards(num_of_blocks, picture, constraint):
#     for row_idx in range(num_of_blocks):
#         if constraint[0] - row_idx < 0:
#             break
#         elif picture[constraint[0] - row_idx][constraint[1]] == 1:
#             continue
#         picture[constraint[0] - row_idx][constraint[1]] = 1
#
#
# def color_downward(num_of_blocks, picture, constraint):
#     for row_idx in range(num_of_blocks):
#         if constraint[0] + row_idx >= len(picture):
#             break
#         elif picture[constraint[0] + row_idx][constraint[1]] == 1:
#             continue
#         picture[constraint[0] + row_idx][constraint[1]] = 1
#
#
# def color_forward(num_of_blocks, picture, constraint):
#     for column_idx in range(num_of_blocks):
#         if constraint[0] + column_idx >= len(picture[0]):
#             break
#         elif picture[constraint[0] + column_idx][constraint[1]]:
#             continue
#         picture[constraint[0] + column_idx][constraint[1]] = 1
#
#
# def color_backward(num_of_blocks, picture, constraint):
#     for column_idx in range(num_of_blocks):