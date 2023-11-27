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
    # EXIT = 3

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

def get_action() -> ActionList:
    """Returns the current actions list"""
    retval = EMPTY_ACTIONLIST
    raw_input = _ev.get()
    if raw_input == "exit":
        raise KeyboardInterrupt
    if raw_input in hotkey_mappings:
        retval = hotkey_mappings[raw_input]
    _ev.clear()
    return retval
