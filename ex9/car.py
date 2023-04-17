class Car:
    """
    the functions and attributes of a given car on the board
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        # implement your code and erase the "pass"
        lst_coordinate = []
        for i in range(self.__length):
            if self.__orientation == 1:
                lst_coordinate.append((self.__location[0], self.__location[1] + i))
            elif self.__orientation == 0:
                lst_coordinate.append((self.__location[0] + i, self.__location[1]))
        return lst_coordinate

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        #For this car type, keys are from 'udrl'
        #The keys for vertical cars are 'u' and 'd'.
        #The keys for horizontal cars are 'l' and 'r'.
        #You may choose appropriate strings.
        # implement your code and erase the "pass"
        #The dictionary returned should look something like this:
        #result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        #A car returning this dictionary supports the commands 'f','d','a'.
        if self.__orientation == 1:
            return {"l":"go left", "r": "go right"}
        elif self.__orientation == 0:
            return {"u": "go up", "d":"go down"}
        else:
            return None
        pass

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        if movekey == None:
            return
        target_cells = []
        if self.__orientation == 0:
            if movekey == 'd':
                target_cells.append((self.__location[0] + self.__length, self.__location[1]))
            elif movekey == 'u':
                target_cells.append((self.__location[0] - 1, self.__location[1]))
        elif self.__orientation == 1:
            if movekey == 'l':
                target_cells.append((self.__location[0], self.__location[1] - 1))
            elif movekey == 'r':
                target_cells.append((self.__location[0], self.__location[1]+ self.__length))
        else:
            return None
        return target_cells

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        # if self.movement_requirements(movekey) == None:
        #     return False
        if not(movekey in self.possible_moves().keys()):
            return False
        if movekey == 'u':
            self.__location = (self.__location[0] - 1, self.__location[1])
        elif movekey == 'd':
            self.__location = (self.__location[0] + 1, self.__location[1])
        elif movekey == 'l':
            self.__location = (self.__location[0], self.__location[1] - 1)
        elif movekey == 'r':
            self.__location = (self.__location[0], self.__location[1] + 1)
        return True



    def get_name(self):
        """
        :return: The name of this car.
        """
        # implement your code and erase the "pass"
        return self.__name
if __name__ == "__main__":
    car = Car("oki", 2, (2,4), 1)
    print(car.movement_requirements("r"))