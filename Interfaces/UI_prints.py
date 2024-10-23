"""
This is where all the filler print functions will be implemented
"""
from Objects.Board import Board


class InputError(Exception):
    pass


class PrintInputConverts:
    @staticmethod
    def game_start():
        """
        Series of prints for the beginning of the game, explanation of the game rules
        :return:
        """
        print("\u001b[95mWelcome to airplanes !! ✈︎ ☆ To start, press \033[1;3mENTER\033[0m\u001b[0m")
        start = input()
        startmessage = "\u001b[95m\033[1;3mLet's get started ! ✈︎ \033[0m \u001b[0m"

        if start == "":
            while True:
                print("\u001b[95mDo you wish to know some \033[1;3mgame rules\033[0m ? (yes/no)\u001b[0m")
                option = input("> ")
                option = option.lower().strip()

                if option == "yes":
                    print("\u001b[95m~~~~~~~~~~~~~~~~~~~~ Alright, here are a few rules: ~~~~~~~~~~~~~~~~~~~~\u001b[0m")
                    print("\033[1;3mWhen placing a plane, you have to keep in mind two main aspects !\033[0m")
                    print("1) First, the plane orientation, whether you want your plane to be facing north, south, east or west (N, S, E or W)")
                    print("2) Then, choose an appropriate board position (example: C2)")
                    print()
                    print("\033[1;3mThen, it's time to take turns trying to hit the opponent's plane !\033[0m")
                    print("1) Hitting a plane's head means the whole plane is destroyed")
                    print("2) A plane is destroyed by either hitting the head of the plane or hitting all of the other cells of the plane")
                    print()
                    print("\033[1;3mThe game ends if you successfully eliminate all the enemy planes, or when all of your planes were destroyed ! :)\033[0m")
                    print()
                    print(startmessage)
                    print("\u001b[95m~ To begin, please select 3 positions for the planes: \u001b[0m")
                    break

                elif option == "no":
                    print(startmessage)
                    print("\u001b[95m~ To begin, please select 3 positions for the planes: \u001b[0m")
                    break

                else:
                    print("\u001b[95mInvalid Input ! \u001b[0m")
                    print()

        else:
            print("\u001b[95mSee you next time ! ⋆｡°✩\u001b[0m")

    @staticmethod
    def get_player_plane():
        """
        Gets the data to add a plane, makes validations regarding the input
        :return: The orientation of the plane and the position of the head of the plane
        """
        plane_orientation = input("\033[1;3mPlease input the orientation of the plane: \033[0m")
        plane_position = input("\033[1;3mPlease input the position of the head of the plane: \033[0m")
        print()

        plane_orientation = plane_orientation.upper().strip()
        plane_position = plane_position.upper().strip()
        orientations = ["N", "S", "W", "E"]

        while plane_orientation not in orientations:
            plane_orientation = input("\033[1;3mPlease input the orientation of the plane: \033[0m")
            plane_position = input("\033[1;3mPlease input the position of the head of the plane: \033[0m")
            print()

            plane_orientation = plane_orientation.upper().strip()
            plane_position = plane_position.upper().strip()

        plane_position = PrintInputConverts.convert_position_input_to_list(plane_position)

        return plane_orientation, plane_position

    @staticmethod
    def get_player_hit():
        """
        Gets player input for where to hit
        :return: The position in list form
        """
        player_hit = input("\033[1;3mWhat's your target ? (Input valid board position) \033[0m")
        player_hit = player_hit.upper().strip()

        player_hit = PrintInputConverts.convert_position_input_to_list(player_hit)

        return player_hit

    @staticmethod
    def convert_position_input_to_list(input_position: str):
        """
        Turns player input (str) into a list
        :param input_position: The string representing the position
        :return: The list with the coordinates
        """
        if len(input_position) == 3:
            position = [x for x in input_position]
            position = position[:2]
            position[1] = "10"
            if not position[0].isalpha() or not position[1].isnumeric():
                raise InputError
        elif len(input_position) == 2:
            position = [x for x in input_position]
            if not position[0].isalpha() or not position[1].isnumeric():
                raise InputError
        else:
            raise InputError

        return position

    @staticmethod
    def print_hit_board(board: Board):
        """
        Prints the board without the planes
        :param board:
        :return:
        """
        hit_board = board.hit_board()

        return hit_board
