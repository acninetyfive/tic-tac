import random


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


class RandomComputer(Player):
    def __init__(self, name, mark, game="basic"):
        super().__init__(name, mark, game)

    def get_move(self):
        x = random.randrange(3)
        y = random.randrange(3)
        if self.game == "basic":
            return (x, y)
        elif self.game == "ultimate":
            b = random.randrange(9)
            return (b, x, y)


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
