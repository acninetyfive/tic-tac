import PySimpleGUI as sg
from engine import Game
from player import Player, RandomComputer


class GUIHuman(Player):
    def __init__(self, name, mark, gui):
        super().__init__(name, mark)
        self.gui = gui

    def get_move(self):
        event, values = self.gui.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            return None
        return event


layout = [[sg.Button('', size=(8, 4), key=(i, j), pad=(1, 1)) for j in range(3)] for i in range(3)]

game_name = "Tic-Tac-Toe"
window = sg.Window(game_name, layout, background_color="BLACK")

p1 = GUIHuman("Gabe", "X", window)
p2 = RandomComputer("Computer", "O")

players = [p1, p2]
game = Game(players, True)

while True:
    curr_move, curr_mark = game.take_turn()

    window[curr_move].update(game.get_board().get_board()[curr_move[0]][curr_move[1]], button_color=('black', 'white'))

    if game.get_result() is not None:
        break

while True:
    e, v = window.read()
    if e in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
