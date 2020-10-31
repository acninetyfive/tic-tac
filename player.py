import random


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark

    def set_mark(self, mark):
        self.mark = mark

    def get_move(self):
        pass


class Human(Player):
    def __init__(self, name, mark):
        super().__init__(name, mark)

    def get_move(self):
        move = input("{0} input your move 'x','y'\n".format(self.mark)).split(",")
        return [int(move[0]), int(move[1])]


class RandomComputer(Player):
    def __init__(self, name, mark):
        super().__init__(name, mark)

    def get_move(self):
        x = random.randrange(3)
        y = random.randrange(3)
        return [x,y]