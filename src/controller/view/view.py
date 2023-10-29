from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
import scrap_engine as se
import csv


def drawBoard():
    matrix = [[]]
    track_cords = []

    screen = se.Map(width=20, height=20, background="+")
    # read file and write to 2d matrix
    # with open("plansza.txt") as file:

    X = se.Object("X", "float", 0)

    b = se.Frame(4, 4)
    b.add_ob(X, 1, 1)
    b.add(screen, 1, 1)
    screen.show()

    # matrix.append(list(line.strip()))

    # with open("track.txt") as file:
    #     for line in file:
    #         track_cords.append(tuple(line.strip().split(' : ')))

    return matrix


def game(screen, matrix):
    for line in range(len(matrix)):
        for c in range(len(matrix[line])):
            screen.print_at(matrix[line][c], line, c)
    while True:
        screen.refresh()
