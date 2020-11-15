class Player:
    def __init__(self, name, mark, game="basic"):
        self.name = name
        self.mark = mark
        self.game = game
        self.moves_list = None
        self.engine = None

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def get_move(self):
        pass

    def get_moves_list(self):
        return self.moves_list

    def set_moves_list(self, moves_list):
        self.moves_list = moves_list

    def set_engine(self, engine):
        self.engine = engine

    def get_engine(self):
        return self.engine
