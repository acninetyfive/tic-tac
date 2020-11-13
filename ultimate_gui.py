import PySimpleGUI as sg

from players.random_computer_player import RandomComputer
from ultimate_engine import UltimateGame
from players.human_players import GUIHuman
from players.pure_monte_carlo_player import PureMonteCarlo

if __name__ == "__main__":
    frame_layouts = [[[sg.Button('', size=(6, 3), key=(k, i, j), pad=(1, 1))
                       for j in range(3)]
                      for i in range(3)]
                     for k in range(9)]

    layout = [[sg.Frame(str(j*3 + i), frame_layouts[j*3 + i], key=(i, j), pad=(6, 6), background_color="BLACK")
               for i in range(3)] for j in range(3)]

    game_name = "Ultimate Tic-Tac-Toe"
    window = sg.Window(game_name, layout, background_color="BLACK")

    p1 = GUIHuman("Gabe", "X", window)
    # p1 = RandomComputer("Random", "X", "ultimate")
    # p2 = GUIHuman("Shannon", "O", window)
    p2 = PureMonteCarlo("Monte", "O", 2, "ultimate")

    symbol_dict = {p1.get_mark(): p1.get_name(), p2.get_mark(): p2.get_name(), "draw": "DRAW"}

    players = [p1, p2]
    game = UltimateGame(players, False)

    p2.set_engine(game)

    while not window.finalize():
        input()

    while True:
        curr_move, curr_mark = game.take_turn()
        print(game.get_board().get_global_proxy_board())
        print(game.get_result())
        print()

        window[curr_move].update(game.get_board().get_global_board()[curr_move[0] // 3][curr_move[0] % 3]
                                 .get_board()[curr_move[1]][curr_move[2]], button_color=('black', 'white'))

        if game.get_board().get_global_board()[curr_move[0] // 3][curr_move[0] % 3].get_status() == curr_mark:
            window[(curr_move[0] % 3, curr_move[0] // 3)].update("WON BY {}".format(curr_mark))
        elif game.get_board().get_global_board()[curr_move[0] // 3][curr_move[0] % 3].get_status() == "draw":
            window[(curr_move[0] % 3, curr_move[0] // 3)].update("DRAWN GAME")

        window.finalize()

        if game.get_result() is not None:
            print("RESULT:", symbol_dict[game.get_result()])
            break

    while True:
        e, v = window.read()
        if e in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()
