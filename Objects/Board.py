"""
This is where anything regarding the board will be implemented
"""
from random import randint

from Objects.Plane import Plane


class BoardError(Exception):
    pass


class Board:
    def __init__(self):
        self.__board = [["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                        ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"]
                        ]
        self.__hit_board = [["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"],
                            ["□", "□", "□", "□", "□", "□", "□", "□", "□", "□"]
                            ]
        self.__number_of_planes = 0
        self.__planes = []  # here I wish to append the planes that are being used,
        # each plane will remember the orientation N, S, W, E and where the head is positioned

    def hit(self, position: list):
        """
        Hits the board, marking it by X if the terrain is empty.
        If the player hit an airplane's head, then the whole plane is destroyed, marked by a red X.
        If the player hit the body of an airplane, then only the hit is marked by a red X.
        :param position: The coordinates of the hit
        :return: Changes the board
        """
        head = ["\u001b[95m▲\u001b[0m", "\u001b[95m▼\u001b[0m", "\u001b[95m▶\u001b[0m", "\u001b[95m◀\u001b[0m"]
        body = "\u001b[95m■\u001b[0m"
        row = ord(position[0]) - ord('A')
        column = int(position[1]) - 1

        if self.__board[row][column] in head:

            if self.__board[row][column] == "\u001b[95m▲\u001b[0m":
                self.__number_of_planes -= 1
                plane = Plane("N", position)
                if plane in self.__planes:
                    self.__planes.remove(plane)

                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                row += 1
                for c in range(column - 2, column + 3):
                    self.__board[row][c] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[row][c] = "\u001b[31mX\u001b[0m"
                row += 1
                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                row += 1
                for c in range(column - 1, column + 2):
                    self.__board[row][c] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[row][c] = "\u001b[31mX\u001b[0m"

            if self.__board[row][column] == "\u001b[95m▼\u001b[0m":
                self.__number_of_planes -= 1
                plane = Plane("S", position)
                if plane in self.__planes:
                    self.__planes.remove(plane)

                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                row -= 1
                for c in range(column - 2, column + 3):
                    self.__board[row][c] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[row][c] = "\u001b[31mX\u001b[0m"
                row -= 1
                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                row -= 1
                for c in range(column - 1, column + 2):
                    self.__board[row][c] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[row][c] = "\u001b[31mX\u001b[0m"

            if self.__board[row][column] == "\u001b[95m▶\u001b[0m":
                self.__number_of_planes -= 1
                plane = Plane("E", position)
                if plane in self.__planes:
                    self.__planes.remove(plane)

                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                column -= 1
                for r in range(row - 2, row + 3):
                    self.__board[r][column] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[r][column] = "\u001b[31mX\u001b[0m"
                column -= 1
                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                column -= 1
                for r in range(row - 1, row + 2):
                    self.__board[r][column] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[r][column] = "\u001b[31mX\u001b[0m"

            if self.__board[row][column] == "\u001b[95m◀\u001b[0m":
                self.__number_of_planes -= 1
                plane = Plane("W", position)
                if plane in self.__planes:
                    self.__planes.remove(plane)

                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                column += 1
                for r in range(row - 2, row + 3):
                    self.__board[r][column] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[r][column] = "\u001b[31mX\u001b[0m"
                column += 1
                self.__board[row][column] = "\u001b[31mX\u001b[0m"
                self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"
                column += 1
                for r in range(row - 1, row + 2):
                    self.__board[r][column] = "\u001b[31mX\u001b[0m"
                    self.__hit_board[r][column] = "\u001b[31mX\u001b[0m"

            return "kill"

        elif self.__board[row][column] == body:
            self.__board[row][column] = "\u001b[31mX\u001b[0m"
            self.__hit_board[row][column] = "\u001b[31mX\u001b[0m"

            for plane in self.__planes:
                if [row, column] in plane.places:
                    plane.places.remove([row, column])
                    plane.number_of_hits -= 1
                    hit_plane = plane

            if hit_plane.number_of_hits == 0:
                if hit_plane in self.__planes:
                    self.__planes.remove(hit_plane)
                    self.__number_of_planes -= 1

                for place in hit_plane.places:
                    r, c = place
                    self.__hit_board[r][c] = "\u001b[31mX\u001b[0m"

                return "kill"

            else:
                return "hit"

        else:
            self.__board[row][column] = "X"
            self.__hit_board[row][column] = "X"

            return "miss"

    def validate_hit(self, position: list):
        """
        Returns True if the position is valid, and False otherwise
        :param position: A position on the board
        :return: True if valid False otherwise
        """
        row = ord(position[0]) - ord('A')
        column = int(position[1]) - 1

        if row not in range(10) or column not in range(10):
            return False

        if self.__board[row][column] in ["X", "\u001b[31mX\u001b[0m"]:
            return False

        return True

    def generate_computer_hit(self):
        row = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        column = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        while True:
            position = [row[randint(0, len(row) - 1)], column[randint(0, len(column) - 1)]]

            if self.validate_hit(position):
                return position

    def generate_computer_hits_nearby(self, previous_hit: list):
        """
        In case the last hit was one that was close to a plane (if hit returned "hit"), then it would make sense
        for the computer to hit a tile nearby the previous hit
        :param previous_hit: The last hit tile position
        :return: A list of possible good hit options
        """
        row = ord(previous_hit[0]) - ord('A')
        column = int(previous_hit[1]) - 1
        row_options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        column_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        previous_hits = []

        for r in range(row - 1, row + 2):
            for c in range(column - 1, column + 2):
                if 0 <= r <= 9 and 0 <= c <= 9:
                    position = [row_options[r], column_options[c]]
                    if self.validate_hit(position):
                        previous_hits.append(position)

        return previous_hits

    def generate_computer_board(self):
        """
        Generates a board for the computer using randomly generated planes
        :return:
        """
        plane1 = Plane("", [])
        plane2 = Plane("", [])
        plane3 = Plane("", [])

        plane1.generate_plane()
        self.place_plane(plane1)

        plane2.generate_plane()
        placed = False
        while not placed:
            try:
                self.check_if_placeable(plane2)
                placed = True
                self.place_plane(plane2)
            except BoardError:
                plane2.generate_plane()

        plane3.generate_plane()
        placed = False
        while not placed:
            try:
                self.check_if_placeable(plane3)
                placed = True
                self.place_plane(plane3)
            except BoardError:
                plane3.generate_plane()

    def check_if_placeable(self, plane: Plane):
        """
        Checks if a plane can be placeable on a certain board, so it doesn't collide with other planes
        :param plane: The plane that we want to place
        :return:
        """
        orientation = plane.orientation
        position = plane.position
        row = ord(position[0]) - ord('A')
        column = int(position[1]) - 1
        occupied = ["\u001b[95m▲\u001b[0m", "\u001b[95m▼\u001b[0m", "\u001b[95m▶\u001b[0m", "\u001b[95m◀\u001b[0m",
                    "\u001b[95m■\u001b[0m"]

        if orientation == "N":
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            row += 1
            for c in range(column - 2, column + 3):
                if self.__board[row][c] in occupied:
                    raise BoardError("You cannot overlap planes !")
            row += 1
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            row += 1
            for c in range(column - 1, column + 2):
                if self.__board[row][c] in occupied:
                    raise BoardError("You cannot overlap planes !")

        elif orientation == "S":
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            row -= 1
            for c in range(column - 2, column + 3):
                if self.__board[row][c] in occupied:
                    raise BoardError("You cannot overlap planes !")
            row -= 1
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            row -= 1
            for c in range(column - 1, column + 2):
                if self.__board[row][c] in occupied:
                    raise BoardError("You cannot overlap planes !")

        elif orientation == "E":
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            column -= 1
            for r in range(row - 2, row + 3):
                if self.__board[r][column] in occupied:
                    raise BoardError("You cannot overlap planes !")
            column -= 1
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            column -= 1
            for r in range(row - 1, row + 2):
                if self.__board[r][column] in occupied:
                    raise BoardError("You cannot overlap planes !")

        elif orientation == "W":
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            column += 1
            for r in range(row - 2, row + 3):
                if self.__board[r][column] in occupied:
                    raise BoardError("You cannot overlap planes !")
            column += 1
            if self.__board[row][column] in occupied:
                raise BoardError("You cannot overlap planes !")
            column += 1
            for r in range(row - 1, row + 2):
                if self.__board[r][column] in occupied:
                    raise BoardError("You cannot overlap planes !")

        return True

    def check_if_won(self):
        """
        If the number of planes is 0, the opposite player won
        :return:
        """
        if self.__number_of_planes == 0:
            return True

        return False

    def place_plane(self, plane: Plane):
        """
        Places a plane on the board
        :param plane: The plane we wish to place
        :return:
        """
        self.__planes.append(plane)
        self.__number_of_planes += 1
        orientation = plane.orientation
        position = plane.position
        row = ord(position[0]) - ord('A')
        column = int(position[1]) - 1
        cube = "\u001b[95m■\u001b[0m"
        places = []

        if orientation == "N":
            self.__board[row][column] = "\u001b[95m▲\u001b[0m"
            places.append([row, column])
            row += 1
            for c in range(column - 2, column + 3):
                self.__board[row][c] = cube
                places.append([row, c])
            row += 1
            self.__board[row][column] = cube
            places.append([row, column])
            row += 1
            for c in range(column - 1, column + 2):
                self.__board[row][c] = cube
                places.append([row, c])

        elif orientation == "S":
            self.__board[row][column] = "\u001b[95m▼\u001b[0m"
            places.append([row, column])
            row -= 1
            for c in range(column - 2, column + 3):
                self.__board[row][c] = cube
                places.append([row, c])
            row -= 1
            self.__board[row][column] = cube
            places.append([row, column])
            row -= 1
            for c in range(column - 1, column + 2):
                self.__board[row][c] = cube
                places.append([row, c])

        elif orientation == "E":
            self.__board[row][column] = "\u001b[95m▶\u001b[0m"
            places.append([row, column])
            column -= 1
            for r in range(row - 2, row + 3):
                self.__board[r][column] = cube
                places.append([r, column])
            column -= 1
            self.__board[row][column] = cube
            places.append([row, column])
            column -= 1
            for r in range(row - 1, row + 2):
                self.__board[r][column] = cube
                places.append([r, column])

        elif orientation == "W":
            self.__board[row][column] = "\u001b[95m◀\u001b[0m"
            places.append([row, column])
            column += 1
            for r in range(row - 2, row + 3):
                self.__board[r][column] = cube
                places.append([r, column])
            column += 1
            self.__board[row][column] = cube
            places.append([row, column])
            column += 1
            for r in range(row - 1, row + 2):
                self.__board[r][column] = cube
                places.append([r, column])

        plane.places = places

    def __str__(self):
        """
        Writes the board in a beautiful pink manner
        :return:
        """
        var = "A"
        str_board = "      1  2  3  4  5  6  7  8  9  10" + "\n"
        str_board += "    ________________________________" + "\n"
        for row in self.__board:
            str_board += var + "   | "
            var = chr(ord(var) + 1)
            for i in range(0, len(row)):
                if i == 9:
                    str_board += str(row[i]) + " "
                else:
                    str_board += str(row[i]) + "  "
            str_board += "|" + "\n"

        str_board += "    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        return str_board

    def hit_board(self):
        """
        This is str representation of the board without the planes
        :return:
        """
        var = "A"
        str_board = "      1  2  3  4  5  6  7  8  9  10" + "\n"
        str_board += "    ________________________________" + "\n"
        for row in self.__hit_board:
            str_board += var + "   | "
            var = chr(ord(var) + 1)
            for i in range(0, len(row)):
                if i == 9:
                    str_board += str(row[i]) + " "
                else:
                    str_board += str(row[i]) + "  "
            str_board += "|" + "\n"

        str_board += "    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        return str_board
