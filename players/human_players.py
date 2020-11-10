import PySimpleGUI as sg

from players.base_player import Player


class CommandLineHuman(Player):
    def __init__(self, name, mark, game="basic"):
        super().__init__(name, mark, game)

    def get_move(self):
        if self.game == "basic":
            move = input("{0} input your move 'x','y'\n".format(self.mark)).split(",")
            return [int(move[0]), int(move[1])]
        elif self.game == "ultimate":
            move = input("{0} input your move 'board #0-8','x','y'\n".format(self.mark)).split(",")
            return [int(move[0]), int(move[1]), int(move[2])]


class GUIHuman(Player):
    def __init__(self, name, mark, gui):
        super().__init__(name, mark)
        self.gui = gui

    def get_move(self):
        event, values = self.gui.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            return None
        return event