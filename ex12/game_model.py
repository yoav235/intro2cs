import ex12_utils
import hint
from boggle import Board



class Model:
    current_word = ""
    score = 0
    found_word_list = []
    last_char_pressed = ''
    last_coor_pressed = (5,5)

    def __init__(self, board):
        self.do_clear()
        self.__board = board



    def type_in(self, c: str) -> None:
        if c in self.__board:








    @staticmethod
    def check_if_word_in_dict(word, dictionary=Controller.DICTIONARY):
        if word in dictionary:
            return True
        return False

    def calculate_score(self):
        return Board.get_points() + ((len(path))**2)

    def check_if_path_valid(self, path):
        return ex12_utils.is_path_legal(ex12_utils.COORDINATES,path)

    def lock_action(self, path, word, current_score):
        if self.check_if_path_valid(path) and self.check_if_word_in_dict(word):





