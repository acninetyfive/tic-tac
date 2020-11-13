import random
from players.base_player import Player
from copy import deepcopy
from operator import itemgetter


class PureMonteCarlo(Player):
    def __init__(self, name, mark, number_of_runs=10, game="basic"):
        super().__init__(name, mark, game)
        self.engine = None
        self.number_of_runs = number_of_runs

    def get_move(self):
        if self.engine is None:  # Engine not set, default to random move
            x = random.randrange(3)
            y = random.randrange(3)
            if self.game == "basic":
                return (x, y)
            elif self.game == "ultimate":
                b = random.randrange(9)
                return (b, x, y)

        before_board = deepcopy(self.engine.get_board())

        active_local_board = self.engine.get_board().get_active_local_board()

        all_move_values = {}
        for r in range(self.number_of_runs):
            for x in range(3):
                for y in range(3):
                    if active_local_board is not None:
                        active_board_to_int = 3 * active_local_board[0] + active_local_board[1]
                        b_range = range(active_board_to_int, active_board_to_int + 1)
                    else:
                        b_range = range(9)

                    for b in b_range:
                        val = self.monte_carlo(b, x, y)
                        if (b, x, y) not in all_move_values:
                            all_move_values[(b, x, y)] = val
                        else:
                            old_avg = all_move_values[(b, x, y)]
                            all_move_values[(b, x, y)] = (val - old_avg)/(r+1)

        best_val = max(all_move_values.values())
        best_moves = filter(lambda m: m[1] == best_val, all_move_values.items())

        if before_board != self.engine.get_board():
            raise ValueError("Board not in original state, rewind failure")
            exit()
        print(all_move_values)
        print(best_val)
        return random.choice(list(best_moves))[0]

    def monte_carlo(self, b, x, y):
        result = self.engine.take_turn((b, x, y))
        if result[0] == "invalid":
            return -1
        elif result[0] == self.mark:
            self.rewind_game(1)
            return 1
        elif result[0] == "draw":
            self.rewind_game(1)
            return 0

        win = 0
        result, moves = self.random_runout()
        if result == self.mark:
            win = 1
        self.rewind_game(moves + 1)
        # self.rewind_game(1)

        return win

    def random_runout(self):
        runout_move_counter = 0
        while self.engine.get_result() is None:
            turn_result = self.engine.take_turn(self.get_random_move())
            while turn_result[0] == "invalid":
                turn_result = self.engine.take_turn(self.get_random_move())
            runout_move_counter += 1

        return self.engine.get_result(), runout_move_counter

    def rewind_game(self, number_of_moves):
        for _ in range(number_of_moves):
            self.engine.undo_turn()

    def get_random_move(self):
        x = random.randrange(3)
        y = random.randrange(3)
        if self.game == "basic":
            return (x, y)
        active_local_board = self.engine.get_board().get_active_local_board()
        if active_local_board is None:
            b = random.randrange(9)
        else:
            b = 3 * active_local_board[0] + active_local_board[1]
        return (b, x, y)

    def set_engine(self, engine):
        self.engine = engine

    def get_engine(self):
        return self.engine
