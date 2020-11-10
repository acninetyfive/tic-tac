class Player:
    def __init__(self, name, mark, game="basic"):
        self.name = name
        self.mark = mark
        self.game = game

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def get_move(self):
        pass
