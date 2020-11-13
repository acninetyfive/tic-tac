from itertools import chain

from simple_board import SimpleBoard


class UltimateBoard:
    def __init__(self, name="Ultimate Tic-Tac-Toe"):
        self.name = name
        local_board_names = [["Top Left", "Top Middle", "Top Right"],
                             ["Middle Left", "Middle Middle", "Middle Right"],
                             ["Bottom Right", "Bottom Middle", "Bottom Right"]]
        self.global_board = [[SimpleBoard(local_board_names[i][j]) for i in range(3)] for j in range(3)]
        self.global_proxy_board = SimpleBoard("Global Proxy")
        self.active_local_board = None
        self.status = None
        self.moves = []

    def move_and_check(self, b: int, x: int, y: int, mark: str):
        current_board_x = b // 3
        current_board_y = b % 3

        if self.active_local_board is not None and (current_board_x, current_board_y) != self.active_local_board:
            return "invalid"
        elif self.global_board[current_board_x][current_board_y].get_status() is not None:
            return "invalid"

        move = self.global_board[current_board_x][current_board_y].move_and_check(x, y, mark)

        if move == "invalid":
            return "invalid"

        self.moves.append((b, x, y, self.active_local_board))

        if self.global_board[x][y].get_status() is None:
            self.active_local_board = (x, y)
        else:
            self.active_local_board = None

        if move == mark:
            global_move = self.global_proxy_board.move_and_check(current_board_x, current_board_y, mark)
            if global_move == mark:
                self.status = mark
                return mark
            elif global_move == "draw":
                self.status = "draw"
                return "draw"

        elif move == "draw":
            global_move = self.global_proxy_board.move_and_check(current_board_x, current_board_y, "D")
            if global_move == "draw":
                self.status = "draw"
                return "draw"

        return "valid"

    def undo_last_move(self):
        last_move = self.moves.pop()
        current_board_x = last_move[0] // 3
        current_board_y = last_move[0] % 3
        self.active_local_board = last_move[3]

        if self.global_board[current_board_x][current_board_y].get_status() is not None:
            self.global_proxy_board.undo_last_move()
            self.status = None
        self.global_board[current_board_x][current_board_y].undo_last_move()

    def get_global_board(self):
        return self.global_board

    def get_active_local_board(self):
        return self.active_local_board

    def get_status(self):
        return self.status

    def get_global_proxy_board(self):
        return self.global_proxy_board

    def get_moves(self):
        return self.moves

    def __str__(self):
        return "\n################\n".join(
            ["\n".join(
                ["#".join(
                    ["|".join(
                        self.global_board[k][i].get_board()[j]
                    ) for i in range(3)]
                ) for j in range(3)]
            ) for k in range(3)])

    def __eq__(self, obj):
        return isinstance(obj, UltimateBoard) and all(
            [x.__eq__(y) for x, y in zip(
                chain.from_iterable([self.global_board[i] for i in range(3)]),
                chain.from_iterable([obj.get_global_board()[j] for j in range(3)]))])


if __name__ == '__main__':
    ub = UltimateBoard()
    print(ub.move_and_check(4, 1, 1, "X"))
    print(ub)
