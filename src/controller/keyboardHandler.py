import threading
from enum import Enum, auto
import sys
import time

# from pynput.keyboard import Key, Listener, Controller
#
# from src.controller.view.view import GameView as GV
#
#
# class KeyboardListener:
#
#     def __init__(self, view: GV):
#         self.view = view
#         self.i = 0
#         self.moves = []
#         self.moves_count = int()
#
#     def on_press(self, key):
#         if key == Key.right:
#             self.i = (self.i + 1) % self.moves_count
#             self.view.set_cursor(self.moves[self.i])
#         elif key == Key.left:
#             self.i = (self.i - 1) % self.moves_count
#             self.view.set_cursor(self.moves[self.i])
#
#     def listen(self, possible_moves: list):
#         self.moves = possible_moves
#         self.moves_count = len(possible_moves)
#         self.view.set_cursor(self.moves[0])
#         # noinspection PyTypeChecker
#         with (Listener(
#                 on_press=self.on_press, ) as listener):
#             listener.join()
#         return self.i

class Action(Enum):
    LEFT = 0
    RIGHT = 1
    SELECT = 2
    HELP = 3
    EXIT = 4

    @property
    def mapping(self):
        """Returns the current mapped char"""
        return get_mapping(self, hotkey_mappings)


class Event:

    def __init__(self, event=""):
        self._ev = event
        self.emit_fn = None

    def get(self):
        """Getter
        RETURNS:
            Current char"""
        return self._ev

    def set(self, event):
        """Setter
        ARGS:
            event: New char"""
        self._ev = event
        self.emit_fn()

    def clear(self):
        """Clears the event"""
        self._ev = ""

    def set_emit_fn(self, emit_fn):
        """Sets the method used to emit events to the timer"""
        self.emit_fn = emit_fn


_ev = Event()


class ActionList(list):

    def triggers(self, *actions):
        """Checks if the self triggers a set of actions"""
        for action in actions:
            if action in self:
                return True
        return False


EMPTY_ACTIONLIST = ActionList()
ACTION_CONTROLS = (Action.LEFT, Action.RIGHT, Action.SELECT, Action.HELP, Action.EXIT)

hotkey_mappings = {
    "Key.left": Action.LEFT,
    "Key.up": Action.LEFT,
    "key.right": Action.RIGHT,
    "key.down": Action.RIGHT,
    "key.space": Action.SELECT,
    "h": Action.HELP,
    '?': Action.HELP,
    'q': Action.EXIT
}


def get_action():
    retval = EMPTY_ACTIONLIST
    raw_input = _ev.get()
    if raw_input == "exit":
        raise KeyboardInterrupt
    if raw_input in hotkey_mappings:
        retval = hotkey_mappings[raw_input]
    _ev.clear()
    return retval


def get_mapping(action, keys):
    for key, action_list in keys.items():
        if action in action_list:
            return key


def test_keyboard():

    if sys.platform == "win32":
        import msvcrt
        while True:
            if msvcrt.kbhit():
                char = msvcrt.getwch()
                if char in ('\000', '\xe0'):
                    arrow = msvcrt.getwch()
                    if arrow == 'H':
                        print('up')
                    elif arrow == 'P':
                        print('down')
                    elif arrow == 'K':
                        print('left')
                    elif arrow == 'M':
                        print('right')
                elif char == ' ':
                    print('space')
                else:
                    print(char)

    else:
        import tty
        import termios
        import select

        global fd, old_settings

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        tty.setraw(fd)
        time.sleep(0.1)

        while True:

                rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
                if rlist:
                    ch = sys.stdin.read(1)
                    print(ch)
                    if ord(ch) == 0:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)





