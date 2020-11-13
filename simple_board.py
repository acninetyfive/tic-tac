class SimpleBoard:

    def __init__(self, name: str = "Tic-Tac-Toe"):
        self.name = name
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.status = None
        self.moves = []

    def move_and_check(self, x: int, y: int, mark: str) -> str:
        if self.status is not None:
            return "invalid"

        if self.board[x][y] != " ":
            return "invalid"

        self.board[x][y] = mark
        self.moves.append((x, y))

        # 'D' Mark is only to be used by the ultimate engine to denote a drawn local game, no win for three D's
        if mark != "D":
            # check column win
            if self.board[(x - 1) % 3][y] == mark and self.board[(x + 1) % 3][y] == mark:
                self.status = mark
                return mark
            # check row win
            if self.board[x][(y - 1 % 3)] == mark and self.board[x][(y + 1) % 3] == mark:
                self.status = mark
                return mark
            # check diagonal win
            if x == y:
                if self.board[(x - 1) % 3][(y - 1) % 3] == mark and self.board[(x + 1) % 3][(y + 1) % 3] == mark:
                    self.status = mark
                    return mark
            # check anti-diagonal win:
            if x + y == 2:
                if self.board[(x - 1) % 3][(y + 1) % 3] == mark and self.board[(x + 1) % 3][(y - 1) % 3] == mark:
                    self.status = mark
                    return mark

        for i in range(3):
            if " " in self.board[i]:
                return "valid"
        self.status = "draw"
        return "draw"

    def undo_last_move(self):
        last_move = self.moves.pop()
        self.board[last_move[0]][last_move[1]] = " "
        if self.status is not None:
            self.status = None

    def get_name(self):
        return self.name

    def get_board(self):
        return self.board

    def get_status(self):
        return self.status

    def get_moves(self):
        return self.moves

    def __str__(self):
        return "|".join(self.board[0]) + "\n" + "|".join(self.board[1]) + "\n" + "|".join(self.board[2])

    def __eq__(self, obj):
        return isinstance(obj, SimpleBoard) and self.board == obj.board
