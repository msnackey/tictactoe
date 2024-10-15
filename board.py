class Board:
    def __init__(self) -> None:
        self.board = []
        self.board_top_rows = [
            "   A   B   C  ",
            "  -----------",
        ]
        self.rows = {
            "1": {
                "A": " ",
                "B": " ",
                "C": " ",
            },
            "2": {
                "A": " ",
                "B": " ",
                "C": " ",
            },
            "3": {
                "A": " ",
                "B": " ",
                "C": " ",
            },
        }
        self.available_cells = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        self.moves = []

    def board_row(self, row) -> str:
        board_row = f""
        i = 0
        for col in row:
            board_row += f" {row[col]} "
            if i < (len(row) - 1):
                board_row += "|"
            i += 1
        return board_row

    def fill_board(self) -> list:
        self.board = []
        for row in self.board_top_rows:
            self.board.append(row)

        i = 0
        for row in self.rows:
            self.board.append(f"{row}|{self.board_row(self.rows[row])}")
            if i < (len(self.rows) - 1):
                self.board.append(" |-----------")
            i += 1

        self.print_board()

    def print_board(self) -> None:
        print("")
        for row in self.board:
            print(row)
        print("")

    def set_cell_value(self, cell, symbol) -> None:
        self.rows[cell[1:]][cell[:1]] = symbol
