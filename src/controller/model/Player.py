from enum import Enum


# [0] : green
# [1] : blue
# [2] : red
# [3] : yellow
class Color(Enum):

    GREEN = 1
    BLUE = 2
    RED = 3
    YELLOW = 4

class Player:   

    def __init__(self, color: Color):
        self.pawns = []
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
        
        self.base


    def get_pawns_location(self):
        return self.pawns, self.pieces_at_base
    
    def set_pawn_location(self, pawn: int, location: int):
        self.pawns[pawn] = location
        
    
        # or maybe
        # for i in range(4):
        #     if self.pawns[i] == pawn:
        #         self.pawns[i] = location
        
    

