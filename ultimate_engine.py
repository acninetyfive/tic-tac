from players.pure_monte_carlo_player import PureMonteCarlo
from ultimate_board import UltimateBoard
from players.random_computer_player import RandomComputer


class UltimateGame:
    def __init__(self, players, verbose=True, name="Tic-Tac-Toe"):
        self.players = players
        self.verbose = verbose
        self.board = UltimateBoard(name)
        self.active_player = 0
        self.move_counter = 0
        self.result = None
        for player in self.players:
            player.set_moves_list(self.board.get_moves())

        if self.verbose:
            print(self.move_counter)
            print(self.board)

    def take_turn(self, move=None):
        faux_move = move is not None  # True if move is being made by ai internally, not in actual game
        if not faux_move:
            move = self.players[self.active_player].get_move()
        status = self.board.move_and_check(move[0], move[1], move[2],
                                           self.players[self.active_player].get_mark())
        while status == "invalid":
            if faux_move:
                return status, self.players[self.active_player].get_mark()
            else:
                pass

            if self.verbose:
                # print("Invalid Move")
                pass
            move = self.players[self.active_player].get_move()
            status = self.board.move_and_check(move[0], move[1], move[2],
                                               self.players[self.active_player].get_mark())

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

        just_played = self.active_player
        self.active_player = (self.active_player + 1) % 2

        return move, self.players[just_played].get_mark()

    def undo_turn(self):
        self.board.undo_last_move()
        self.active_player = (self.active_player + 1) % 2
        self.move_counter -= 1
        self.result = self.board.get_status()
        # print("turn undone, new counter:", self.move_counter)

    def set_board(self, board):
        self.board = board

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

    # p1 = GUIHuman("Gabe", "X", window)
    p1 = RandomComputer("Random", "X", "ultimate")
    # p2 = GUIHuman("Shannon", "O", window)
    p2 = PureMonteCarlo("Monte", "O", 10, "ultimate")

    symbol_dict = {"X": "Random", "O": "Monte", "draw": "DRAW"}

    players = [p1, p2]

    game = UltimateGame(players, False)

    p2.set_engine(game)

    while game.get_result() is None:
        turn = game.take_turn()
        print(game.get_board().get_global_proxy_board())
        print()

    print("RESULT:", symbol_dict[game.get_result()])
