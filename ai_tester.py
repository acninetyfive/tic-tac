from ultimate_engine import UltimateGame
from players.random_computer_player import RandomComputer
from players.pure_monte_carlo_player import PureMonteCarlo
from os import remove

if __name__ == "__main__":
    games = 100

    # p1 = RandomComputer("Random", "X", "ultimate")
    p1 = PureMonteCarlo("Monte-5", "X", 10, "ultimate")
    # p2 = RandomComputer("Random2", "O", "ultimate")
    p2 = PureMonteCarlo("Monte-10", "O", 10, "ultimate")

    symbol_dict = {p1.get_mark(): p1.get_name(), p2.get_mark(): p2.get_name(), "draw": "DRAW"}

    players = [p1, p2]

    results = [0, 0, 0]

    for i in range(games):
        game = UltimateGame([players[i % 2], players[(i + 1) % 2]], False)

        p2.set_engine(game)

        j = 0
        while game.get_result() is None:
            turn = game.take_turn()

        print("RESULT:", symbol_dict[game.get_result()])
        if game.get_result() == p1.get_mark():
            results[0] += 1
        elif game.get_result() == p2.get_mark():
            results[1] += 1
        elif game.get_result() == "draw":
            results[2] += 1

    print()
    print(p1.get_name(), results[0])
    print(p2.get_name(), results[1])
    print("draw", results[2])
