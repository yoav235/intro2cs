from game_parameters import WIDTH, HEIGHT, get_random_bomb_data
from helper import MOVES_DICT


class Bomb:
    def __init__(self):
        """
        the constructor of object from class Bomb
        self.location: where the bomb is placed on the board.
        self.old_location: where the bomb were on the board
        self.time: how much loops before it explodes.
        self.radius: how far is the shockwave gonna go from the bomb.
        """
        x, y, radius, time = get_random_bomb_data()
        self.location = [(x, y)]
        self.old_location = set()
        self.time = time
        self.radius = radius
        self.cur_radius = 0

    def bomb_round(self):
        """
        this function manages the bomb in a single round of the game
        :return: None
        """
        if self.time == 0:
            self.location = self.explosion()
            self.cur_radius += 1
        else:
            self.time -= 1

    def explosion(self):
        """
        this function calculates the cells which the bomb blast is currently in
        :return: a list contianing all of the cells the explotion is in
        """
        new_location = set()
        for cell in self.location:
            self.old_location.add(cell)
            for direction in MOVES_DICT.values():
                new_location.add((cell[0] + direction[0], cell[1] + direction[1]))
        return list(new_location - self.old_location)

    def get_coordinates(self):
        """
        returns the bomb coordinates
        :return: a list containing the coordinates of the bomb
        """
        return self.location

    def get_old_coordinates(self):
        """
        returns the coordinates the bomb has already been in
        :return: a list containing the bomb's old coordinates
        """
        return list(self.old_location)

    def is_max_radius(self):
        """
        this method checked if the bomb blast has reached its maximum radius
        :return: True if the bomb has reached its maximum radius and false otherwise
        """
        return self.cur_radius == self.radius



