from Player import Color

class Tile:

    def __init__(self,index):
        self.occupied = False
        self.player = None
        self.count = 0
        self.index = index
    def put_pon(self,pon: Color):
        self.occupied = True
        self.player = pon
        self.count += 1

    def remove_pon(self):
        self.count -= 1

        if self.count == 0:
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