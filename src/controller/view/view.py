import scrap_engine as se
from termcolor import colored
import colorama
import src.controller.view.view_classes as vc
from typing import Any, List
from math import floor


def drawBoard(players: int):
    track_cords = []
    track = []
    colorama.init()
    # [0] : green
    # [1] : blue
    # [2] : red
    # [3] : yellow
    home_lines = [[] for x in range(5)]
    pawns = [[] for x in range(players)]

    base: List = [[] for x in range(players)]

    screen = se.Map(background=" ")
    with open("resources/track.txt") as file:
        for line in file:
            track_cords.append(tuple(line.strip().split(' : ')))

    for i in range(len(track_cords)):
        tile = se.Frame(3, 5, state="float")
        tile.add(screen, int(track_cords[i][0]), int(track_cords[i][1]))
        track.append(tile)

    with open("resources/home_tracks.txt") as file:
        for count, line in enumerate(file):
            x, y = line.strip().split(' : ')
            # tile = se.Frame(3, 5, horizontal_chars=['*', '*'],
            #                 vertical_chars=[colored('*', "red"), '*'], corner_chars='*',
            #                 state="float")
            tile = vc.HomeLineTile(floor(count / 4))

            tile.add(screen, int(x), int(y))
            home_lines[floor(count / 4)].append(tile)

    finish = se.Frame(3, 5, corner_chars=("╔", "╗", "╚", "╝"), state="solid")
    finish.add(screen, 20, 12)

    with open("resources/home_base.txt") as file:
        for count, line in enumerate(file):
            if count < players:
                x, y = line.strip().split(' : ')
                base[count] = vc.Base(count)
                base[count].add(screen, int(x), int(y))

    for i in range(players):
        match i:
            case 0:
                for j in range(4):
                    pawn = se.Object(vc.get_colored(i, "G"))
                    pawns[i].append(pawn)
            case 1:
                for j in range(4):
                    pawn = se.Object(vc.get_colored(i, "B"))
                    pawns[i].append(pawn)
            case 2:
                for j in range(4):
                    pawn = se.Object(vc.get_colored(i, "R"))
                    pawns[i].append(pawn)
            case 3:
                for j in range(4):
                    pawn = se.Object(vc.get_colored(i, "Y"))
                    pawns[i].append(pawn)

    screen.show()

    return track, home_lines, finish, pawns


def game(screen, matrix):
    for line in range(len(matrix)):
        for c in range(len(matrix[line])):
            screen.print_at(matrix[line][c], line, c)
    while True:
        screen.refresh()
