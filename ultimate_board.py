from tic_tac_board import TicTacBoard


class UltimateBoard:
    def __init__(self, name="Ultimate Tic-Tac-Toe"):
        self.name = name
        local_board_names = [["Top Left", "Top Middle", "Top Right"],
                             ["Middle Left", "Middle Middle", "Middle Right"],
                             ["Bottom Right", "Bottom Middle", "Bottom Right"]]
        self.global_board = [[TicTacBoard(local_board_names[i][j]) for i in range(3)] for j in range(3)]
        self.global_proxy_board = TicTacBoard("Global Proxy")
        self.active_local_board = None
        self.status = None

    def move_and_check(self, b: int, x: int, y: int, mark: str):
        current_board_x = b // 3
        current_board_y = b % 3

        if self.active_local_board is not None and (current_board_x, current_board_y) != self.active_local_board:
            return "invalid"
        elif self.global_board[current_board_x][current_board_y].get_status() is not None:
            return "invalid"
        else:
            move = self.global_board[current_board_x][current_board_y].move_and_check(x, y, mark)
            if self.global_board[x][y].get_status() is None:
                self.active_local_board = (x, y)
            else:
                self.active_local_board = None

        if move == mark:
            global_move = self.global_proxy_board.move_and_check(current_board_x, current_board_y, mark)
            if global_move == mark:
                self.status = mark
                return mark
        '''
        if move == mark:
            gb = self.get_local_board_statuses()
            for i in range(3):
                print(gb[i])
            # input()
            # check column win
            if self.global_board[(current_board_x - 1) % 3][current_board_y].get_status() == mark and \
                    self.global_board[(current_board_x + 1) % 3][current_board_y] == mark:
                self.status = mark
                return mark
            # check row win
            if self.global_board[current_board_x][(current_board_y - 1 % 3)] == mark and \
                    self.global_board[current_board_x][(current_board_y + 1) % 3] == mark:
                self.status = mark
                return mark
            # check diagonal win
            if current_board_x == current_board_y:
                if self.global_board[(current_board_x - 1) % 3][(current_board_y - 1) % 3] == mark and \
                        self.global_board[(current_board_x + 1) % 3][(current_board_y + 1) % 3] == mark:
                    self.status = mark
                    return mark
            # check anti-diagonal win:
            if current_board_x + current_board_y == 2:
                if self.global_board[(current_board_x - 1) % 3][(current_board_y + 1) % 3] == mark and \
                        self.global_board[(current_board_x + 1) % 3][(current_board_y - 1) % 3] == mark:
                    self.status = mark
                    return mark
        '''
        for i in range(3):
            for j in range(3):
                if self.global_board[i][j].get_status() is None:
                    return "valid"

        self.status = "draw"
        return "draw"

    def get_global_board(self):
        return self.global_board

    def get_active_local_board(self):
        return self.active_local_board

    def get_status(self):
        return self.status

    def get_global_proxy_board(self):
        return self.global_proxy_board

    def __str__(self):
        return "\n################\n".join(
            ["\n".join(
                ["#".join(
                    ["|".join(
                        self.global_board[k][i].get_board()[j]
                    ) for i in range(3)]
                ) for j in range(3)]
            ) for k in range(3)])


if __name__ == '__main__':
    ub = UltimateBoard()
    print(ub.move_and_check(4, 1, 1, "X"))
    print(ub)
