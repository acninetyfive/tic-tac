import random
from players.base_player import Player


class PureMonteCarlo(Player):
    def __init__(self, name, mark, game="basic"):
        super().__init__(name, mark, game)
        self.engine = None
        self.number_of_runs = 10

    def get_move(self):
        if self.engine is None:  # Engine not set, default to random move
            x = random.randrange(3)
            y = random.randrange(3)
            if self.game == "basic":
                return (x, y)
            elif self.game == "ultimate":
                b = random.randrange(9)
                return (b, x, y)

        active_local_board = self.engine.get_board().get_active_local_board()

        best_moves = None
        best_val = None
        for x in range(3):
            for y in range(3):
                if active_local_board is not None:
                    b = 3 * active_local_board[0] + active_local_board[1]
                    val = self.monte_carlo(b, x, y)
                    if best_moves is None:
                        best_moves = [(b, x, y)]
                        best_val = val
                    elif val > best_val:
                        best_moves = [(b, x, y)]
                        best_val = val
                    elif val == best_val:
                        best_moves.append((b, x, y))
                else:
                    for b in range(9):
                        val = self.monte_carlo(b, x, y)
                        if best_moves is None:
                            best_moves = [(b, x, y)]
                            best_val = val
                        elif val > best_val:
                            best_moves = [(b, x, y)]
                            best_val = val
                        elif val == best_val:
                            best_moves.append((b,x , y))

        return random.choice(best_moves)

    def monte_carlo(self, b, x, y):
        # print()
        # print()
        # print("prior moves ", self.moves_list)
        result = self.engine.take_turn((b, x, y))
        # print("initial", b,x,y,result)
        if result[0] == "invalid":
            return -1

        wins = 0
        for _ in range(self.number_of_runs):
            result, moves = self.random_runout()
            if result == self.mark:
                wins += 1
            # print("runout: ", result, moves)
            self.rewind_game(moves)
            # print("moves after rewind", self.moves_list)

        self.rewind_game(1)

        return wins/self.number_of_runs

    def random_runout(self):
        # print("moves before runout", self.moves_list)
        runout_move_counter = 0

        turn_result = self.engine.take_turn(self.get_random_move())
        while turn_result[0] == "invalid":
            turn_result = self.engine.take_turn(self.get_random_move())
        runout_move_counter += 1

        while self.engine.get_result() is None:
            turn_result = self.engine.take_turn(self.get_random_move())
            while turn_result[0] == "invalid":
                turn_result = self.engine.take_turn(self.get_random_move())
            runout_move_counter += 1
            # print("runout while", turn_result, self.engine.get_result())

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
