class Board:

    def __init(self, players:list):
        self.players = players
        self.board = []
        for i in range(41):
            board.append(Tile(i))


    def move(self):