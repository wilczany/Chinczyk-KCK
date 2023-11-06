from Player import Color

class Tile:

    def __init__(self,index):
        self.occupied = False
        self.player = None
        self.index = index
    def put_pon(self,pon: Color):
        self.occupied = True
        self.player = pon

    def remove_pon(self):
        self.occupied = False
        self.player = None


    def can_move(self, color: Color):
        if self.player == color:
            return True
        else:
            return False

    def can_put(self,color: Color):
        if self.occupied == False or self.player == color:
            return True
        else:
            return False