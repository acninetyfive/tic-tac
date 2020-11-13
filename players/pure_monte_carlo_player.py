import random
from players.base_player import Player
from copy import deepcopy


class PureMonteCarlo(Player):
    def __init__(self, name, mark, number_of_runs=10, game="basic"):
        super().__init__(name, mark, game)
        self.engine = None
        self.number_of_runs = number_of_runs
        # print(self.number_of_runs)

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
        before_moves = self.engine.get_move_counter()

        active_local_board = self.engine.get_board().get_active_local_board()

        best_moves = None
        best_val = None
        all_move_values = {}
        for x in range(3):
            for y in range(3):
                if active_local_board is not None:
                    active_board_to_int = 3 * active_local_board[0] + active_local_board[1]
                    b_range = range(active_board_to_int, active_board_to_int + 1)
                else:
                    b_range = range(9)

                for b in b_range:
                    # print()
                    # print("monte move:", (b, x, y))
                    # print("pre monte move counter", self.engine.get_move_counter())
                    val = self.monte_carlo(b, x, y)
                    # print("post monte move counter", self.engine.get_move_counter())
                    # print()
                    all_move_values[(b, x, y)] = val
                    if best_moves is None:
                        best_moves = [(b, x, y)]
                        best_val = val
                    elif val > best_val:
                        best_moves = [(b, x, y)]
                        best_val = val
                    elif val == best_val:
                        best_moves.append((b, x, y))
        # for key in all_move_values:
        #    print(key, all_move_values[key])
        # print()
        # print(best_moves)
        # print("before moves:", before_moves, "after moves", self.engine.get_move_counter())
        # print("board check", before_board == self.engine.get_board())
        if before_board != self.engine.get_board():
            print('jjjj')
            exit()
        # t = input()
        # if t == "p":
        #     print()
        #     print("before board")
        #     print(before_board)
        #     print("after board")
        #     print(self.engine.get_board())
        #     input()

        return random.choice(best_moves)

    def monte_carlo(self, b, x, y):
        # print("PRE INITIAL TURN")
        result = self.engine.take_turn((b, x, y))
        # print("POST INITIAL TURN", result)
        if result[0] == "invalid":
            # self.rewind_game(1)
            return -1
        elif result[0] == self.mark:
            self.rewind_game(1)
            return 1
        elif result[0] == "draw":
            self.rewind_game(1)
            return 0

        wins = 0
        for _ in range(self.number_of_runs):
            # print("PRE runout moves:", self.engine.get_move_counter())
            result, moves = self.random_runout()
            # print("POST RUNOUT")
            if result == self.mark:
                wins += 1
            self.rewind_game(moves)
            # print("runout moves:", moves, "new counter:", self.engine.get_move_counter())

        self.rewind_game(1)

        return wins/self.number_of_runs

    def random_runout(self):
        # # print("moves before runout", self.moves_list)
        # runout_move_counter = 0
        # m = self.get_random_move()
        # print("runout move 1", m)
        # turn_result = self.engine.take_turn(m)
        # print("result 1", turn_result)
        # # print("FIRST RUNOUT RESULT", turn_result)
        # while turn_result[0] == "invalid":
        #     turn_result = self.engine.take_turn(self.get_random_move())
        #     # print("Pre runout turn", self.engine.get_board().get_moves()[-1])
        #     print("WHILE LOOP TURN RESULT", turn_result, self.engine.get_board().get_active_local_board())
        #     # print(self.engine.get_board().get_global_proxy_board())
        #     # print(self.engine.get_board())
        #     # print(self.engine.get_result())
        # print("EXITED WHILE")
        # runout_move_counter += 1
        runout_move_counter = 0
        while self.engine.get_result() is None:
            turn_result = self.engine.take_turn(self.get_random_move())
            while turn_result[0] == "invalid":
                turn_result = self.engine.take_turn(self.get_random_move())
            runout_move_counter += 1
            # print("runout while", runout_move_counter, turn_result, self.engine.get_result())

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
