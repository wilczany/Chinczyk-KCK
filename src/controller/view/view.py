import scrap_engine as se
import colorama
import src.controller.view.view_classes as vc
from typing import List
from math import floor



class GameView:
    def __init__(self, players: int):
        self.track_cords = []
        self.track = []

        # [0] : green
        # [1] : blue
        # [2] : red
        # [3] : yellow

        self.home_lines = [[] for _ in range(4)]
        self.pawns = [[] for _ in range(players)]

        self.base = []

        self.cursor_pos = None

        colorama.init()
        # initiate map

        self.screen = se.Map(background=" ")
        with open("resources/track.txt") as file:
            for line in file:
                self.track_cords.append(tuple(line.strip().split(' : ')))

        # draw track

        for i in range(len(self.track_cords)):
            if i == 0:
                tile = vc.Tile(0)
            elif i % 10 == 0:
                x = i / 10
                if x == 1:
                    tile = vc.Tile(2)
                elif x == 2:
                    tile = vc.Tile(1)
                else:
                    tile = vc.Tile(3)
            else:
                tile = vc.Tile()
            tile.add(self.screen, int(self.track_cords[i][0]), int(self.track_cords[i][1]))
            self.track.append(tile)

        # draw inner track

        with open("resources/home_tracks.txt") as file:
            for count, line in enumerate(file):
                x, y = line.strip().split(' : ')
                tile = vc.HomeLineTile(floor(count / 4))

                tile.add(self.screen, int(x), int(y))
                self.home_lines[floor(count / 4)].append(tile)

        finish = se.Frame(3, 5, corner_chars=("╔", "╗", "╚", "╝"), state="solid")
        finish.add(self.screen, 20, 12)

        # draw base

        with open("resources/home_base.txt") as file:
            for count, line in enumerate(file):
                x, y = line.strip().split(' : ')
                self.base.append(vc.Base(count))
                self.base[count].add(self.screen, int(x), int(y))

        # draw pawns

        for i in range(players):
            for j in range(4):
                pawn = vc.Pawn(i)
                self.pawns[i].append(pawn)
                self.base[i].add_pawn(pawn)

        self.screen.show()
        # return track, home_lines, finish, pawns

    def move(self, tile_out: int, tile_in: int):
        pwn = self.track[tile_out].remove_pawn()
        self.track[tile_in].add_pawn(pwn)

    def move_from_base(self, color: int, tile: int):
        pwn = self.base[color].remove_pawn()
        self.track[tile].add_pawn(pwn)
        self.screen.show()

    def move_to_home_tiles(self, tile_out, color, tile_in):
        pass

    def move_to_base(self, tile):
        pwn = self.track[tile].remove_pawn()
        self.base[pwn.color].add_pawn(pwn)

        self.screen.show()

    def set_cursor(self, tile_selected: int):
        # 1. could make a var to store cursor place
        # 2. does not work in home tiles
        # 3. does not work in base xd
        # 4. need to find a way to pass arguments from controller
        # to this function to work with 2. and 3.
        # Passing tiles is no go.

        if self.cursor_pos is not None:
            self.track[self.cursor_pos].pawn.cursor_switch()
        self.track[tile_selected].pawn.cursor_switch()
        self.cursor_pos = tile_selected

        self.screen.show()


def game(screen, matrix):
    for line in range(len(matrix)):
        for c in range(len(matrix[line])):
            screen.print_at(matrix[line][c], line, c)
    while True:
        screen.refresh()
