from tic_tac_board import TicTacBoard
from player import CommandLineHuman, RandomComputer


class SimpleGame:
    def __init__(self, players, verbose=True, name="Tic-Tac-Toe"):
        self.players = players
        self.verbose = verbose
        self.board = TicTacBoard(name)
        self.active_player = 0
        self.move_counter = 0
        self.result = None

        if self.verbose:
            print(self.move_counter)
            print(self.board)

    def take_turn(self):
        move = self.players[self.active_player].get_move()
        status = self.board.move_and_check(move[0], move[1], self.players[self.active_player].get_mark())
        while status == "invalid":
            if self.verbose:
                print("Invalid move")
            move = self.players[self.active_player].get_move()
            status = self.board.move_and_check(move[0], move[1], self.players[self.active_player].get_mark())

        if status != "valid":
            self.result = status

        self.move_counter += 1

        if self.verbose:
            print(self.move_counter)
            print(self.board)

        if status == self.players[self.active_player].get_mark():
            if self.verbose:
                print("{0} WINS!".format(self.players[self.active_player].get_name()))
        elif status == "draw":
            if self.verbose:
                print("It's a draw!")
        elif status == "valid":
            pass

        self.active_player = (self.active_player + 1) % 2

        return move, self.players[self.active_player].get_mark()

    def get_board(self):
        return self.board

    def get_players(self):
        return self.players

    def get_move_counter(self):
        return self.move_counter

    def get_active_player(self):
        return self.active_player

    def get_result(self):
        return self.result


if __name__ == '__main__':
    a = RandomComputer("Computer_X", "X")
    b = RandomComputer("Computer_O", "O")

    game = SimpleGame([a, b])

    while game.get_result() is None:
        game.take_turn()
