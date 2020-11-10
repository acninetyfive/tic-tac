import random

from players.base_player import Player


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
