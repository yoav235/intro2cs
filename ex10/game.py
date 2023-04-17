from bomb import Bomb
from game_parameters import WIDTH, HEIGHT
from apple import Apple


class Game:
    def __init__(self, snake):
        """
        this function initiates a game object
        :param snake: a snake object of a given length in a given location
        """
        self.snake = snake
        self.score = 0
        self.bomb = self.__place_bomb(self.snake)
        self.apples = self.__place_apples(self.snake)

    def __place_apples(self, snake):
        """
        this function creates the apple list so that the apples are not inside the snake body
        :param snake: a snake object containing the snake object
        :return: a list contianing three apple objects not inside the snake
        """
        apple_lst = list()
        apple_location_lst = list()
        for ind in range(3):
            apple = Apple()
            while apple.get_location() in snake.location() or \
                    apple.get_location() in apple_location_lst or \
                    apple.get_location() in self.bomb_location():
                apple = Apple()
            apple_lst.append(apple)
            apple_location_lst.append(apple.get_location())
        return apple_lst

    def get_apple_locations(self):
        """
        this function returns a tuple list contains the coordinates of the game's apples
        :return: a list of tuples containing the locaiton of the apples
        """
        location_lst = list()
        for apple in self.apples:
            location_lst.append(apple.get_location())
        return location_lst

    def __place_bomb(self, snake):
        """
        this method places a bomb in an empty spot on the board both in the constructor and in game
        :param snake: a snake object containing the game's snake
        :return: a bomb object that is not inside the snake
        """
        bomb = Bomb()
        while bomb.location[0] in snake.location():
            bomb = Bomb()
        return bomb

    def single_round(self, key_clicked, does_grow):
        """
        this function performs a single round of the game
        :param key_clicked: a string containing the name of the key that was pressed
        and None if no key was pressed
        :param does_grow: a bool type that states whether the snake will start growing in this round
        :return: a tuple containing a bool type that states True if the game is over and False otherwise
        and an int containing the amount of rounds the snake has to keep growing in
        """
        cur_snake_length = self.snake.get_length()
        self.snake.move(key_clicked, does_grow, self.bomb_location())
        self.__apple_eaten()
        self.bomb.bomb_round()
        if self.bomb.is_max_radius() or self.is_bomb_out_of_bounds():
            self.bomb = self.__place_bomb(self.snake)
        return self.is_game_over(cur_snake_length)

    def is_bomb_out_of_bounds(self):
        """
        this function checked if the bomb blast is out of bounds
        :return: True if the bomb blast is out of bounds and false otherwise
        """
        out_of_bounds = False
        for location in self.bomb_location():
            if location[0] >= WIDTH or location[0] < 0 or location[1] >= HEIGHT or location[1] < 0:
                out_of_bounds = True
                break
        return out_of_bounds

    def __apple_eaten(self):
        """
        this functions checks whether the apple is eaten and updates the game accordingly
        :return: None
        """
        for apple in self.apples:
            if apple.get_location() in self.snake_location():
                self.score += apple.score
                self.__replace_apple(apple)
            elif apple.get_location() in self.bomb_location():
                self.__replace_apple(apple)

    def __replace_apple(self, apple_to_replace):
        """
        this function replaces the eaten apple with a new apple that is not inside the snake's body
        :param apple_to_replace: the apple that was eaten
        :return: None
        """
        for ind, apple in enumerate(self.apples):
            if apple_to_replace == apple:
                new_apple = Apple()
                while (new_apple in self.snake_location()) or (new_apple in self.bomb_location()):
                    new_apple = Apple()
                self.apples[ind] = new_apple

    def current_score(self):
        """
        this function returns the current game score
        :return: an int containing the current score
        """
        return self.score

    def apples_location(self):
        """
        this functions returns the location of all of the apples on the board
        :return: a list containing the coordinates of all of the apples
        """
        cell_lst = list()
        for apple in self.apples:
            cell_lst.append(apple.get_location())
        return cell_lst

    def snake_location(self):
        """
        this function returns the location of the snake
        :return: a list containing the coordinates of all of the cells the snake is currently in
        """
        return self.snake.location()

    def bomb_location(self):
        """
        this function returns the location of the bomb
        :return: a list containing the coordinates that the bomb is in
        """
        return self.bomb.get_coordinates()

    def is_game_over(self, cur_snake_length):
        """
        this functions checks whether the game is over after the current round
        :return: True if the game is over and False otherwise
        """
        game_over = False
        snake_head = self.snake.get_head_location()
        snake_location = self.snake.location()
        if self.snake.get_length() < cur_snake_length:
            game_over = True
        elif snake_head in snake_location[1:]:
            game_over = True
        elif self.does_snake_hit_bomb():
            game_over = True
        elif self.snake.get_length() >= (WIDTH * HEIGHT) - 3:
            game_over = True
        return game_over

    def does_snake_hit_bomb(self):
        """
        this function checks if the snake hits the bomb
        :return: True if the snake hits the bomb or its blast and false otherwise
        """
        snake_hit_bomb = False
        bomb_blast = self.bomb_location()
        for cell in self.snake_location():
            if cell in bomb_blast:
                snake_hit_bomb = True
                break
        return snake_hit_bomb
