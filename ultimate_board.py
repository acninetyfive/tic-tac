from tic_tac_board import TicTacBoard


class UltimateBoard:
    def __init__(self, name="Ultimate Tic-Tac-Toe"):
        self.name = name
        local_board_names = [["Top Left", "Top Middle", "Top Right"],
                             ["Middle Left", "Middle Middle", "Middle Right"],
                             ["Bottom Right", "Bottom Middle", "Bottom Right"]]
        self.global_board = [[TicTacBoard(local_board_names[i][j]) for i in range(3)] for j in range(3)]

    def get_global_board(self):
        return self.global_board

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
    print(ub)
