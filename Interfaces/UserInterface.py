"""
This is where anything regarding output/input will be implemented, as well as the game start
"""
from random import randint

from Objects.Board import Board, BoardError
from Interfaces.UI_prints import PrintInputConverts, InputError
from Objects.Plane import Plane, PlaneError


class UI:
    def __init__(self):
        self.computer_board = Board()
        self.player_board = Board()
        self.computer_board.generate_computer_board()
        self.Print_Input = PrintInputConverts()

    def set_player_board(self):
        planes = 0
        print()
        print(self.player_board)
        print()
        while planes < 3:
            try:
                plane_orientation, plane_position = self.Print_Input.get_player_plane()
                plane = Plane(plane_orientation, plane_position)
                plane.check_plane()

                if self.player_board.check_if_placeable(plane):
                    self.player_board.place_plane(plane)
                    print("\u001b[95mPlane placed successfully !\u001b[0m")
                    if planes != 2:
                        print()
                        print(self.player_board)
                        print()
                    planes += 1

            except PlaneError as pe:
                print(pe)
                print("Please provide a valid plane orientation and position: ")
            except BoardError as be:
                print(be)
            except InputError as ie:
                print("Invalid plane placement!")

    def game_loop(self):
        print()
        print("\u001b[95mGreat ! Let the game start !\u001b[0m")
        nearby_hits = []

        while True:
            if not self.computer_board.check_if_won() or not self.player_board.check_if_won():
                player_hit = PrintInputConverts.get_player_hit()
                while not Board.validate_hit(self.computer_board, player_hit):
                    print("Please choose a valid tile ! ")
                    player_hit = PrintInputConverts.get_player_hit()

                self.computer_board.hit(player_hit)
                print()
                print("This is the opponent's board :")
                print()
                print(PrintInputConverts.print_hit_board(self.computer_board))
                print()

            if self.computer_board.check_if_won():
                print()
                print("You've won !")
                break
            if self.player_board.check_if_won():
                print()
                print("The computer won.")
                break

            if not self.computer_board.check_if_won() or not self.player_board.check_if_won():
                if len(nearby_hits) == 0:
                    computer_hit = self.player_board.generate_computer_hit()
                    result = self.player_board.hit(computer_hit)
                    if result == "hit":
                        nearby_hits = self.player_board.generate_computer_hits_nearby(computer_hit)
                else:
                    computer_hit = nearby_hits[randint(0, len(nearby_hits) - 1)]
                    result = self.player_board.hit(computer_hit)

                    if result == "kill":
                        nearby_hits.clear()
                    elif result == "hit":
                        new_possible_hits = self.player_board.generate_computer_hits_nearby(computer_hit)
                        for h in new_possible_hits:
                            if h not in nearby_hits:
                                nearby_hits.append(h)
                        nearby_hits.remove(computer_hit)
                    elif result == "miss":
                        nearby_hits.remove(computer_hit)

                print("This is your board :")
                print(self.player_board)

            if self.computer_board.check_if_won():
                print("You've won ! Yippy !")
                break
            if self.player_board.check_if_won():
                print("The computer won ... Womp womp womp...")
                break

    def main(self):
        try:
            self.Print_Input.game_start()
            self.set_player_board()
            print()
            print("These are your planes ! ✈︎ ")
            print()
            print(self.player_board)

            self.game_loop()

        except InputError as ie:
            print(ie)


if __name__ == "__main__":
    start = UI()
    start.main()
