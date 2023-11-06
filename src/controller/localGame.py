import random

import curses
from curses import wrapper
import view.view as v
import model as m
class LocalGame:

    def __init__(self, players: int):

        self.view = v.GameView(players)

        self.base = [
            m.base(m.Color.GREEN)
        ]

