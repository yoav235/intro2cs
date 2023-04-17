# from boggle_board_randomizer import randomize_board
from ex12_utils import *
import ex12_utils_vr2
import boggle
import time

words = list(open("tiny_data.txt"))
# for i in range(len(words)):
#     words[i]= words[i][::-2]
board = [['W', 'S', 'OW', 'W'],
         ['O', 'H', 'I', 'N'],
         ['A', 'S', 'O', 'W'],
         ['S', 'E', 'E', 'O']]
# y = find_length_n_paths(2,board,["sow"])
# x = max_score_paths(board, words)
# print(len(x))
# print(find_length_n_words(4, board, words))
# print(x)
# print(y)
gogo = boggle.Board()
gogo.run()