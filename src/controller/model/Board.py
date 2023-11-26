from Player import Color
from Tile import Tile


class Board:
    EMPTY = 0

    def __init(self, playersCount: int):
        self.board = [ 0 for i in range(40) ] # 40 tiles
        


        for i in playersCount:
            self.camp.append(Color(1))


    def get_moves(self, color: Color, dice: int):
        tab = []
        can_move_from_base = False
        p_pawns, p_at_base = self.get_pawns_location(color)

        if p_at_base > 0 and dice ==6:
            can_move_from_base = True
        
        for i in range(len(p_pawns)):

        
        return tab, can_move_from_base


class FinishLine:

    def __init__(self, color: Color):
        self.color == color

    # TODO
    # WYMYŚL CO ZORBIC - WYDAJE SIE CIEZKIE XD