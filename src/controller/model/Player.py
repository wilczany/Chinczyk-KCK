from enum import IntEnum, IntFlag, Enum


# [0] : green
# [1] : blue
# [2] : red
# [3] : yellow
class Color(Enum):
    GREEN = 0
    BLUE = 1
    RED = 2
    YELLOW = 3


class Player:

    def __init__(self, color: Color):
        self.pawns = [Pawn(color.value) for i in range(4)]
        self.steps = [0, 0, 0, 0]
        self.start = int()
        self.pieces_at_base = 4
        match color:
            case Color.GREEN:
                self.start = 0
            case Color.BLUE:
                self.start = 20
            case Color.RED:
                self.start = 10
            case Color.YELLOW:
                self.start = 30

    def get_pawns_location(self):
        postitions = []
        for p in self.pawns:
            postitions.append(p.position)

    def set_pawn_location(self, pawn: int, location: int):

        for i in range(4):
            if self.pawns[i].position == pawn:
                pass

        # or maybe
        # for i in range(4):
        #     if self.pawns[i] == pawn:
        #         self.pawns[i] = location

    def pawn_start(self):

        tmp = [self.start if x == -1 else x for x in self.pawns]

    def pawn_kicked_out(self, position: int):

        tmp = [-1 if x == position else x for x in self.pawns]
        self.pawns = tmp

    def get_pawns(self):
        return self.pawns


class Pawn:

    def __init__(self, color: int):
        self.steps = 0
        self.at_base = True
        self.Finished = False
        self.position = -1
        self.color = color

    def start(self, start: int):
        self.at_base = False
        self.position = start

    def move(self, dice: int):
        self.steps += dice
        self.position = (self.position + dice) % 40

    def knocked_out(self):
        self.at_base = True
        self.position = -1
        self.steps = 0

    def next_move_finish(self, dice: int):
        return self.steps + dice == 44

    def next_move_home(self, dice: int):
        return 44 >= self.steps + dice >= 40
