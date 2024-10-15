import random

from board import Board
from player import Player

logo = r"""
___________.__         ___________               ___________            
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
  |    |   |  \  \___    |    |   / __ \\  \___    |    |(  <_> )  ___/ 
  |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                   \/                 \/     \/                      \/ """


class Game:
    def __init__(self) -> None:
        self.logo = logo
        self.description = "This is the game of Tic Tac Toe. \nWhen it's your turn, you can choose a cell (e.g. A1, B3, C2, etc.) to make your move. \n\
When one player has achieved three cells in a row, they are declared the winner.\n"
        self.active = True

        print(self.logo)
        print(self.description)

    def set_board(self) -> None:
        self.board = Board()

    def set_players(self) -> None:
        self.players = []
        self.players.append(Player(input("What is the name of player 1? "), "X"))
        self.players.append(Player(input("What is the name of player 2? "), "O"))

    def set_starting_player(self) -> None:
        self.active_player = random.choice(self.players)
        print(f"{self.active_player.name} begins!")

    def get_move(self) -> None:
        player = self.active_player
        move = input(
            f"{player.name} ({player.symbol}): Where do you want to make your move? "
        )
        if move.upper() in list(
            set(self.board.available_cells) - set(self.board.moves)
        ):
            self.board.set_cell_value(move.upper(), player.symbol)
            self.board.moves.append(move.upper())
        elif move.upper() in self.board.available_cells:
            print("Cell is not available. Try again.")
            self.get_move()
        else:
            print("Not a valid entry. Try again.")
            self.get_move()

    def check_win_condition(self) -> bool:
        winning_combinations = [
            ["A1", "A2", "A3"],
            ["B1", "B2", "B3"],
            ["C1", "C2", "C3"],
            ["A1", "B1", "C1"],
            ["A2", "B2", "C2"],
            ["A3", "B3", "C3"],
            ["A1", "B2", "C3"],
            ["A3", "B2", "C1"],
        ]
        for combi in winning_combinations:
            winning_combination = False
            for cell in combi:
                if self.board.rows[cell[1:]][cell[:1]] != self.active_player.symbol:
                    winning_combination = False
                    break
                else:
                    winning_combination = True
            if winning_combination:
                self.active_player.score += 1
                print(f"{self.active_player.name} won!")
                print(
                    f"The score is {self.players[0].name}: {self.players[0].score} - {self.players[1].name}: {self.players[1].score}.\n"
                )
                return True
        return False

    def check_end_condition(self) -> bool:
        if len(list(set(self.board.available_cells) - set(self.board.moves))) == 0:
            print("The game ended in a draw.")
            return True
        else:
            return False

    def check_active(self) -> None:
        if self.check_win_condition() or self.check_end_condition():
            self.active = False

    def change_active_player(self) -> None:
        self.active_player = (self.players + [False])[
            self.active_player == self.players[0]
        ]
