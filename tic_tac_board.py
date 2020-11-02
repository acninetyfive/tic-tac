class Board:

    def __init__(self, name: str = "Tic-Tac-Toe"):
        self.name = name
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def move_and_check(self, x: int, y: int, mark: str) -> str:
        if self.board[x][y] != " ":
            return "invalid"
        else:
            self.board[x][y] = mark

            # check column win
            if self.board[(x - 1) % 3][y] == mark and self.board[(x + 1) % 3][y] == mark:
                return mark
            # check row win
            if self.board[x][(y - 1 % 3)] == mark and self.board[x][(y + 1) % 3] == mark:
                return mark
            # check diagonal win
            if x == y:
                if self.board[(x - 1) % 3][(y - 1) % 3] == mark and self.board[(x + 1) % 3][(y + 1) % 3] == mark:
                    return mark
            # check anti-diagonal win:
            if x + y == 2:
                if self.board[(x - 1) % 3][(y + 1) % 3] == mark and self.board[(x + 1) % 3][(y - 1) % 3] == mark:
                    return mark

            for i in range(3):
                if " " in self.board[i]:
                    return "valid"
            return "draw"

    def get_name(self):
        return self.name

    def get_board(self):
        return self.board

    def __str__(self):
        return "|".join(self.board[0]) + "\n" + "|".join(self.board[1]) + "\n" + "|".join(self.board[2])
