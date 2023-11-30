# from src.controller.view.menu import App

if __name__ == "__main__":

    # *******************************
    # *          TESTING            *
    # *******************************

    # import src.view.menu as m
    # import src.view.view as v
    # import src.model.board as b
    # import src.view.view_classes as vc

    # menu = m.Menu().run()
    # view = v.GameView(4)
    # board = b.Board(4)

    # *******************************
    # *          TESTING            *
    # *******************************

    import src.localGame as localGame
    import src.view.menu as m
    import curses

    stdscr = curses.initscr()

    menu = m.Menu().run()
    if not m.GameParams.run:
        exit(0)
    
    arr = m.GameParams().players_names

    game = localGame.LocalGame(arr)
    game.start()
