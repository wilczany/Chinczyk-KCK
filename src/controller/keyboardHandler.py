from pynput.keyboard import Key, Listener, Controller

from src.controller.view.view import GameView as GV


class KeyboardListener:

    def __init__(self, view: GV):
        self.view = view
        self.i = 0
        self.moves = []
        self.moves_count = int()

    def on_press(self, key):
        if key == Key.right:
            self.i = (self.i + 1) % self.moves_count
            self.view.set_cursor(self.moves[self.i])
        elif key == Key.left:
            self.i = (self.i - 1) % self.moves_count
            self.view.set_cursor(self.moves[self.i])

    def listen(self, possible_moves: list):
        self.moves = possible_moves
        self.moves_count = len(possible_moves)
        self.view.set_cursor(self.moves[0])
        # noinspection PyTypeChecker
        with (Listener(
                on_press=self.on_press, ) as listener):
            listener.join()
        return self.i
