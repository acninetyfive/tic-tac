from ultimate_engine import UltimateGame
from players.random_computer_player import RandomComputer
from players.pure_monte_carlo_player import PureMonteCarlo
from os import remove

if __name__ == "__main__":
    games = 100

    p1 = RandomComputer("Random", "X", "ultimate")
    # p2 = RandomComputer("Random2", "O", "ultimate")
    p2 = PureMonteCarlo("Monte", "O", 1, "ultimate")

    symbol_dict = {p1.get_mark(): p1.get_name(), p2.get_mark(): p2.get_name(), "draw": "DRAW"}

    players = [p2, p1]

    results = [0, 0, 0]

    for i in range(games):
        game = UltimateGame(players, False)

        p2.set_engine(game)

        game_file = open("game_file.txt", "w")
        j = 0
        while game.get_result() is None:
            # print("pre_turn")
            # print()
            turn = game.take_turn()
            # print(game.get_move_counter())
            # print(game.get_board())
            # game_file.write("\npre board print\n")
            # game_file.write(str(game.get_board()))
            # game_file.write("\n\n")
            # print("pre global proxy print")
            # game_file.write(str(game.get_board().get_global_proxy_board()))
            # game_file.write("\n\n")
            # game_file.write(str(game.get_board().get_moves()[-1]))
            # game_file.write("\n\n\n")
            # print("file wrote", i)
            j += 1
            # print(game.get_board().get_global_proxy_board())
            # print()

        print("RESULT:", symbol_dict[game.get_result()])
        game_file.close()
        remove("game_file.txt")
        if game.get_result() == "X":
            results[0] += 1
        elif game.get_result() == "O":
            results[1] += 1
        elif game.get_result() == "draw":
            results[2] += 1

    print(results)
