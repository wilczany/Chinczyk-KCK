import random

import curses
from curses import wrapper
import view.view as v
import model as m
class LocalGame:

    def __init__(self, players: int):

        self.view = v.GameView(players)

        self.base = []

        for i in range(players):
    #         class Color(Enum):

    # GREEN = 1
    # BLUE = 2
    # RED = 3
    # YELLOW = 4
            self.base.append(m.base())
