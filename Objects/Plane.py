"""
This is where anything related to a plane will be implemented
"""

from random import randint


class PlaneError(Exception):
    pass


class Plane:
    def __init__(self, orientation: str, position: list):
        self.__orientation = orientation
        self.__position = position
        self.__number_of_hits = 10
        self.__places = []
        # a list of string characters, where the first element is the row and the 2nd the column

    @property
    def orientation(self):
        return self.__orientation

    @property
    def position(self):
        return self.__position

    @property
    def number_of_hits(self):
        return self.__number_of_hits

    @number_of_hits.setter
    def number_of_hits(self, new_number_of_hits):
        self.__number_of_hits = new_number_of_hits

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, new_places: list):
        self.__places = new_places

    def generate_plane(self):
        """
        Generates a random plane in a valid position
        :return:
        """
        possible_orientations = ["N", "S", "E", "W"]
        possible_row_position = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.__orientation = possible_orientations[randint(0, 3)]
        self.__position = []

        if self.__orientation == "N":
            self.__position.append(possible_row_position[randint(0, 6)])
            self.__position.append(str(randint(3, 8)))
        elif self.__orientation == "S":
            self.__position.append(possible_row_position[randint(3, 9)])
            self.__position.append(str(randint(3, 8)))
        elif self.__orientation == "E":
            self.__position.append(possible_row_position[randint(2, 7)])
            self.__position.append(str(randint(4, 10)))
        elif self.__orientation == "W":
            self.__position.append(possible_row_position[randint(2, 7)])
            self.__position.append(str(randint(1, 7)))

    def check_plane(self):
        """
        Checks if a plane can be placed in a certain position
        :return:
        """
        row = self.__position[0]
        column = self.__position[1]
        if self.__orientation == "N":
            if row == "H" or row == "I" or row == "J":
                raise PlaneError("Invalid Plane Placement ! ")
            elif column == "1" or column == "2" or column == "9" or column == "10":
                raise PlaneError("Invalid Plane Placement ! ")
        elif self.__orientation == "S":
            if row == "A" or row == "B" or row == "C":
                raise PlaneError("Invalid Plane Placement ! ")
            elif column == "1" or column == "2" or column == "9" or column == "10":
                raise PlaneError("Invalid Plane Placement ! ")
        elif self.__orientation == "E":
            if row == "A" or row == "B" or row == "I" or row == "J":
                raise PlaneError("Invalid Plane Placement ! ")
            elif column == "1" or column == "2" or column == "3":
                raise PlaneError("Invalid Plane Placement ! ")
        elif self.__orientation == "W":
            if row == "A" or row == "B" or row == "I" or row == "J":
                raise PlaneError("Invalid Plane Placement ! ")
            elif column == "8" or column == "9" or column == "10":
                raise PlaneError("Invalid Plane Placement ! ")

    def __eq__(self, other):
        """
        Override the equality comparison to compare planes based on their attributes.
        """
        return (
                isinstance(other, Plane) and
                self.orientation == other.orientation and
                self.position == other.position
        )
