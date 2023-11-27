import src.controller.model.Player as P


class Board:
    EMPTY = 0
    OCCUPIED = [1, 2, 3, 4]

    def __init__(self, players_count: int):

        # 0 - empty
        # 1 - green
        # 2 - blue
        # 3 - red
        # 4 - yellow

        self.board = [0 for i in range(40)]  # 40 tiles
        self.playersCount = players_count
        self.players = [P.Player(P.Color(i)) for i in range(players_count)]

        self.startingTiles = [0, 20, 10, 30]

    def get_moves(self, color: int, dice: int):
        # tab = []
        # can_move_from_base = False
        # p_pawns = self.players[color].get_pawns_location()
        #
        # start = self.players[color].start
        #
        # if dice == 6 and -1 in p_pawns and self.board[start] != self.OCCUPIED[color]:
        #     # wyrzucone 6 & pionki w bazie & pole startowe nie zajete przez wlasny pionek
        #     can_move_from_base = True
        #
        # # for pawn_position in p_pawns:
        #
        # #     if pawn_position == -1:
        # #         # pionek w bazie
        # #         continue
        #
        # #     tile_next = (pawn_position + dice) % 40
        #
        # #     if start == 0:
        # #         #if pawn_position >= start < tile_next:
        # #         if pawn_position >= start and start < tile_next:
        # #          # The pawn has completed a loop
        # #             tab.append(pawn_position)
        # #             continue
        # #     elif pawn_position < start <= tile_next:
        # #     # The pawn has completed a loop
        # #             tab.append(pawn_position)
        #
        # #     elif self.board[tile_next] == self.EMPTY:
        # #         # pole puste
        # #         tab.append(pawn_position)
        #
        # #     elif self.board[tile_next] != self.OCCUPIED[color]:
        # #         # pole zajęte przez innego gracza
        # #         tab.append(pawn_position)
        #
        # #     else:
        # #         # pole zajęte przez tego samego gracza
        # #         continue

        tab = []

        pawns = self.players[color].get_pawns()
        from_base = False
        for pawn in pawns:
            if dice == 6 and not from_base and pawn.at_base:
                tab.append(pawn)
                from_base = True
                continue

            position = pawn.position
            next_position = (position + dice) % 40

            if self.board[next_position] == self.EMPTY:
                tab.append(pawn)

            elif self.board[next_position] != self.OCCUPIED[color+1]:
                tab.append(pawn)


        return tab

    def move(self, color: int, pawn: P.Pawn, dice: int):
        old_position = pawn.position
        new_position = (pawn.position + dice) % 40
        self.board[old_position] = self.EMPTY

        

        if new_tile_state in self.OCCUPIED:
            self.players[new_tile_state - 1].remove_pawn(new_position)
    
    def move_from_base(self, color: int):
        self.board[self.startingTiles[color]] = color + 1
        
        self.players[color].pawn_start()




class FinishLine:
    pass
    # def __init__(self, color: P.Color):
    #     self.color == color

    # TODO
    # WYMYŚL CO ZORBIC - WYDAJE SIE CIEZKIE XD
