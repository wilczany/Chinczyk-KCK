# from src.controller.view.menu import App
from src.controller.view.view import GameView
from src.controller.view.view import game
import scrap_engine as se
from time import sleep

import src.controller.keyboardHandler as keyhandler

import src.controller.view.menu as menu

import src.controller.model.Board as B

import src.controller.model.Player as P

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
    #
    # view.move_to_base(dec)

    # m = menu.Menu()
    # m.run()

    # plrs = menu.GameParams.players_count = 3
    # view = GameView(plrs)

    # view = GameView(3)
    #
    # board = B.Board(3)
    #
    # while True:
    #     tab = board.get_moves(0, 6)
    #     key_in = keyhandler.KeyboardListener(view)
    #     pawn_to_move = key_in.listen(tab)
    #     if pawn_to_move.at_base:
    #         board.move_from_base(0)
    #     else:
    #         board.move(0, pawn_to_move, 6)

    keyboard = keyhandler.KeyboardListener([])
    keyboard.listen([])
