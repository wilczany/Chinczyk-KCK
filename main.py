# from src.controller.view.menu import App
from src.controller.view.view import GameView
from src.controller.view.view import game
import scrap_engine as se
from time import sleep

import src.controller.keyboardHandler as keyhandler

import src.controller.view.menu as menu


if __name__ == "__main__":
    # view = GameView(3)
    # view.move_from_base(0, 0)
    # sleep(2)
    # view.move_from_base(1, 1)
    # view.move_from_base(2, 2)
    # view.move_from_base(0, 3)
    #
    # tab = [0, 3]
    #
    # key_in = keyhandler.KeyboardListener(view)
    # dec = key_in.listen(tab)
    #
    # view.move_to_base(dec)

    m = menu.Menu()
    m.run()

    plrs = menu.GameParams.players_count = 3
    view = GameView(plrs)
    #xddd

