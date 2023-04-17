from ex12_utils import max_score_paths
# from boggle import Board, DICTIONARY
import random

class Hint:
    def __init__(self, board, chosed_path):
        self.__paths = max_score_paths(board, DICTIONARY)
        self.__chosed_paths = chosed_path

    def hint(self):
        for path in self.__paths:
            if path in self.__chosed_paths:
                continue








