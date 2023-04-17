from helper import Node,MOVES_DICT
from game_parameters import HEIGHT,WIDTH


class Snake:
    def __init__(self, length,  head, direction) -> None:
        """
        constructor for the snake class
        :param length: an int that specifies the length of the snake
        :param head: the head of al inked list where each cell has a tuple with coordinates of a cell
        :param direction: a string that specifies the starting direction of a snake
        """
        self.head = Node(head)
        self.length = length
        cur = self.head
        for i in range(1, self.length):
            cur.next = Node((head[0], head[1] - i))
            cur = cur.next
        self.tail = cur
        self.direction = direction

    def get_head_location(self):
        """
        returns a tuple that contains the location of the head of the snake
        :return: a tuple that contains the locations of the snake's head
        """
        return self.head.data

    def does_direction_change(self, direction: str) -> bool:
        """
        this functions checks whether the direction of the snake changes according the
        the direction the user has input
        :param direction: a string specifying the direction the user has inputted
        :return: True if the direction changes and False otherwise
        """
        direction_change = True
        if direction is None:
            direction_change = False
        elif self.direction == direction:
            direction_change = False
        elif self.direction == 'Up' and direction == 'Down':
            direction_change = False
        elif self.direction == 'Down' and direction == 'Up':
            direction_change = False
        elif self.direction == 'Left' and direction == 'Right':
            direction_change = False
        elif self.direction == 'Right' and direction == 'Left':
            direction_change = False
        return direction_change

    def move_head(self, cell_change):
        """
        this functions adds the new head locations according
        :param cell_change: a tuple that contains the change of the coordinates
        :return: None
        """
        new_head_location = self.head.data[0] + cell_change[0], self.head.data[1] + cell_change[1]
        new_head = Node(new_head_location, self.head)
        self.head = new_head

    def move_tail(self):
        """
        this function removes the last cell of the snake body
        :return: None
        """
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        self.tail = cur
        cur.next = None

    def move(self, direction: (str, None), does_grow: bool,bomb_location):
        """
        this function moves the snake in the the specified direction
        :param direction: a string that contains the direction the user has inputted
        :return: None
        """
        cell_change = MOVES_DICT[self.direction]
        if self.does_direction_change(direction):
            cell_change = MOVES_DICT[direction]
            self.direction = direction
        if self.does_snake_collide(bomb_location):
            self.length -= 1
        else:
            self.move_head(cell_change)
        if not does_grow:
            self.move_tail()
        else:
            self.length += 1

    def does_snake_collide(self, bomb_location):
        """
        this function checks if the snake hits an object or its head is outside of the board
        :param bomb_location: a tuple containing the bomb's locaiton
        :return: True if one of the condition
        """
        new_x_location = self.get_head_location()[0] + MOVES_DICT[self.direction][0]
        new_y_location = self.get_head_location()[1] + MOVES_DICT[self.direction][1]
        does_collide = False
        if new_x_location < 0 or new_x_location >= WIDTH or new_y_location < 0 or new_y_location >= HEIGHT:
            does_collide = True
        if (new_x_location, new_y_location) in bomb_location:
            does_collide = True
        return does_collide

    def get_direction(self):
        """
        returns the direction which the snake is moving
        :return: "Left", "Right", "Up" or "Down"
        """
        return self.direction

    def get_length(self):
        """
        returns the current length of the snake
        :return: an int containing the length of the snake
        """
        return self.length

    def location(self):
        """
        this functions returns a list of the cells the snake is in
        :return: a list of tuples containing the cells that currently contain the nsakes
        """
        cell_lst = list()
        cur = self.head
        while cur is not None:
            cell_lst.append(cur.data)
            cur = cur.next
        return cell_lst


