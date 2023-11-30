# from src.controller.view.menu import App
from src.controller.view.view import GameView

if __name__ == "__main__":

    # *******************************
    # *          TESTING            *
    # *******************************

    # from src.controller.keyboardHandler import Action, GetUserAction
    #
    # view = GameView(4)
    #
    # view.move_from_base(0)
    # view.move_from_base(1)
    # view.move_from_base(2)
    # view.move_from_base(3)
    #
    # view.move_to_home(0, 0, 0)
    # view.move_to_home(1, 20, 0)
    # tab = [[0, 0], [-1, 1], [0, 1], [-1, 3], [10,], [30,]]
    #
    # # tab = [1,10,20,30]
    # ln = len(tab)
    # pos = 0
    # action = None
    #
    # view.set_cursor(*tab[pos])
    #
    # ac = GetUserAction()
    # while action != Action.SELECT:
    #
    #     action = ac.get_action()
    #     if action == Action.LEFT:
    #         pos = (pos - 1) % ln
    #         view.set_cursor(*tab[pos])
    #
    #     elif action == Action.RIGHT:
    #         pos = (pos + 1) % ln
    #         view.set_cursor(*tab[pos])
    #
    # exit(0)
    
    # *******************************
    # *          TESTING            *
    # *******************************

    import src.controller.localGame as localGame
    import src.controller.view.menu as m

    menu = m.Menu().run()
    if not m.GameParams.run:
        exit(0)
    
    arr = m.GameParams().players_names

    game = localGame.LocalGame(arr)
    game.start()


