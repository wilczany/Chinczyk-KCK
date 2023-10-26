from Player import Color
from Tile import Tile


class Board:

    def __init(self, playersCount: int):
        self.board = []
        self.camp = []
        for i in playersCount:
            self.camp.append(Color(1))

        for i in range(41):
            self.board.append(Tile(i))

    def get_moves(self, color: Color, dice: int) -> [int]:
        tab = []

        # TODO
        # if dice == 6:
        #     dodaj wyjscie z bazy

        for tile in self.board:
            if tile.can_move():
                tab.append(tile.index)

        return tab


class FinishLine:

    def __init__(self, color: Color):
        self.color == color

    # TODO
    # WYMYŚL CO ZORBIC - WYDAJE SIE CIEZKIE XD