import copy
import car

class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.__board = []
        for i in range(7):
            self.__board.append([])
            for j in range(7):
                self.__board[i].append(None)
        self.__board[3].append(None)
        self.__cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        #The game may assume this function returns a reasonable representation
        #of the board for printing, but may not assume details about it.
        return str(self.__board)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        #In this board, returns a list containing the cells in the square
        #from (0,0) to (6,6) and the target cell (3,7)
        lst_of_cells = []
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                lst_of_cells.append((i,j))
        return lst_of_cells

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        #From the provided example car_config.json file, the return value could be
        #[('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]

        moves = []
        for car in self.__cars:
            for key, vaule in car.possible_moves().items():
                if self.is_car_on_edge(car) == key:
                    continue
                if self.is_car_blocked(car) == key:
                    continue
                moves.append((car.get_name(), key, vaule))
        return moves

    def is_car_blocked(self,car):
        dirction = car.possible_moves().keys()
        car_length = len(car.car_coordinates()) - 1
        car_head = car.car_coordinates()[0]
        car_butt = car.car_coordinates()[car_length]
        for spot in dirction:
            if spot == "r":
                if self.cell_content((car_butt[0],car_butt[1] + 1)) != None:
                    return spot
            if spot == "l":
                if self.cell_content((car_head[0],car_head[1] - 1)) != None:
                    return spot
            if spot == "u":
                if self.cell_content((car_head[0] - 1, car_head[1])) != None:
                    return spot
            if spot == "d":
                if self.cell_content((car_butt[0] + 1, car_butt[1])):
                    return spot

    def is_car_on_edge(self, car):
        for coordinate in car.car_coordinates():
            if coordinate[0] == 0:
                return "u"
            elif coordinate[0] == len(self.__board[coordinate[1]]) - 1:
                return "d"
            elif coordinate[1] == 0:
                return "l"
            elif coordinate[1] == len(self.__board) - 1:
                return "r"



    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        #In this board, returns (3,7)
        return (3,7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        if coordinate == None:
            return None
        if coordinate == (3,7):
            return self.__board[3][7]
        return self.__board[coordinate[0]][coordinate[1]]

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        if car == None:
            return False
        for coordinate in car.car_coordinates():
            if self.if_car_out_of_bounds(coordinate):
                print("error, car is out of bounds")
                return False
            if self.cell_content(coordinate) != None:
                print("there's already a car there")
                return False
        for legal_car in self.__cars:
            if car.get_name() == legal_car.get_name():
                return False
            for coordinate in car.car_coordinates():
                for legal_coordinate in legal_car.car_coordinates():
                    if coordinate == legal_coordinate:
                        return False
        self.__cars.append(car)
        for coordinate in car.car_coordinates():
            self.__board[coordinate[0]][coordinate[1]] = car.get_name()
        return True


    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        moved_car = None
        for car in self.__cars:
            if name == car.get_name():
                moved_car = car
                break
        if moved_car == None:
            print("this car doesn't exist in this board")
            return False
        i_want_to_move_there = moved_car.movement_requirements(movekey)
        for coordinate in i_want_to_move_there:
            if self.if_car_out_of_bounds(coordinate):
                print("out of bounds")
                return False
            if self.cell_content(coordinate) != None:
                print("there's already a car here")
                return False
        # update the board according to the car movement
        copy_car = copy.deepcopy(moved_car)
        copy_car.move(movekey)
        for coordinate in copy_car.car_coordinates():
            if self.if_car_out_of_bounds(coordinate):
                print("the car can't move out out of the board")
                return False
        for coordinate in moved_car.car_coordinates():
            self.__board[coordinate[0]][coordinate[1]] = None
        for car in self.__cars:
            if name == car.get_name():
                self.__cars.remove(car)
        moved_car.move(movekey)
        return self.add_car(moved_car)

    def if_car_out_of_bounds(self, coordinate):
        if coordinate == (3,7):
            return False
        return coordinate[0] >= len(self.__board[0]) or coordinate[1] >= len(self.__board) or coordinate[0] < 0 or \
                coordinate[1] < 0


if __name__ == "__main__":
    board = Board()
    winning_car = car.Car("O", 3, (0,4),1)
    board.add_car(winning_car)
    print(board.move_car("O", "r"))


# board = Board()
# print(board.cell_list())