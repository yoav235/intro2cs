from puzzle_solver import *
picture = [[-1, 0, 1, -1], [0, 1, -1, 1]]
# print(max_seen_cells(picture, 0, 0))
# print(max_seen_cells(picture, 1, 0))
# print(max_seen_cells(picture, 1, 2))
# print(max_seen_cells(picture, 1, 1))

# print(min_seen_cells(picture, 0, 0))
# print(min_seen_cells(picture, 1, 0))
# print(min_seen_cells(picture, 1, 2))
# print(min_seen_cells(picture, 1, 1))

picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1]]
picture2 = [[0, 0, 1, 1], [0, 1, 1, 1]]
# print(check_constraints(picture1, {(0, 1, 1), (1, 1, 1), (1, 0, 1)}))
# print(check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}))
# print(check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}))

# print(solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}, 3, 4))
# print(solve_puzzle({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4))
# print(solve_puzzle({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3))

# print(how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (2, 3, 5)}, 3, 4))
# print(how_many_solutions({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 1)}, 3, 4))
# print(how_many_solutions({(0, 2, 3), (1, 1, 4), (2, 2, 5)}, 3, 3))
# print(how_many_solutions({(i, j, 0) for i in range(3) for j in range(3)}, 3, 3))
print(how_many_solutions(set(), 2, 2))
# print(how_many_solutions({(0, 3, 3), (2, 0, 1)}, 3, 4))