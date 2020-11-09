import PySimpleGUI as sg
import time
from ultimate_engine import UltimateGame
from player import GUIHuman, RandomComputer

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
    # p1 = RandomComputer("Computer1", "X", "ultimate")
    p2 = GUIHuman("Shannon", "O", window)
    # p2 = RandomComputer("Computer", "O", "ultimate")

    color_dict = {"X": "red", "O": "green"}

    players = [p1, p2]
    game = UltimateGame(players, True)

    while not window.finalize():
        input()

    while True:
        #time.sleep(.5)
        curr_move, curr_mark = game.take_turn()

        window[curr_move].update(game.get_board().get_global_board()[curr_move[0] // 3][curr_move[0] % 3]
                                 .get_board()[curr_move[1]][curr_move[2]], button_color=('black', 'white'))

        if game.get_board().get_global_board()[curr_move[0] // 3][curr_move[0] % 3].get_status() == curr_mark:
            window[(curr_move[0] % 3, curr_move[0] // 3)].update("WON BY {}".format(curr_mark))
        elif game.get_board().get_global_board()[curr_move[0] // 3][curr_move[0] % 3].get_status() == "draw":
            window[(curr_move[0] % 3, curr_move[0] // 3)].update("DRAWN GAME")


        window.finalize()

        if game.get_result() is not None:
            break

    while True:
        e, v = window.read()
        if e in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()
