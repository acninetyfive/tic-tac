from simple_board import SimpleBoard
from players.random_computer_player import RandomComputer


class SimpleGame:
    def __init__(self, players, verbose=True, name="Tic-Tac-Toe"):
        self.players = players
        self.verbose = verbose
        self.board = SimpleBoard(name)
        self.active_player = 0
        self.move_counter = 0
        self.result = None
        for player in self.players:
            player.set_moves_list(self.board.get_moves())

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

    def undo_turn(self):
        self.board.undo_last_move()
        self.active_player = (self.active_player + 1) % 2
        self.move_counter -= 1

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

    # a.set_moves_list(game.get_board().get_moves())
    # b.set_moves_list(game.get_board().get_moves())

    while game.get_result() is None:
        game.take_turn()
        test = input()
        if test == "undo":
            game.undo_turn()
        if test == "m":
            print(a.get_moves_list())
