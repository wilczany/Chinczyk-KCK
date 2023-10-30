import scrap_engine as se
import curses


def drawBoard(players: int):
    track_cords = []
    track = []

    # [0] : green
    # [1] : blue
    # [2] : red
    # [3] : yellow
    home_lines = [[] for x in range(5)]
    pawns = [[] for x in range(players)]
    base = [[] for x in range(players)]

    screen = se.Map(background=" ")
    with open("resources/track.txt") as file:
        for line in file:
            track_cords.append(tuple(line.strip().split(' : ')))

    for i in range(len(track_cords)):
        tile = se.Frame(3, 5, state="float")
        tile.add(screen, int(track_cords[i][0]), int(track_cords[i][1]))
        track.append(tile)

    with open("resources/home_lines.txt") as file:
        for line in file:
            for i in range(5):
                x, y = line.strip().split(' : ')
                tile = se.Frame(3, 5, horizontal_chars=['*', '*'],
                                vertical_chars=['*', '*'], corner_chars='*',
                                state="float")

                tile.add(screen, int(x), int(y))
                home_lines[i].append(tile)

    finish = se.Frame(3, 5, corner_chars=("╔", "╗", "╚", "╝"), state="solid")
    finish.add(screen, 20, 12)

    with open ("resources/home_base.txt") as file:
        for line in file:
            for i in range(players):



    for i in range(players):
        match i:
            case 0:
                for j in range(4):
                    pawn = se.Object("G")
                    pawns[i].append(pawn)
            case 1:
                for j in range(4):
                    pawn = se.Object("B")
                    pawns[i].append(pawn)
            case 2:
                for j in range(4):
                    pawn = se.Object("R")
                    pawns[i].append(pawn)
            case 3:
                for j in range(4):
                    pawn = se.Object("Y")
                    pawns[i].append(pawn)
    screen.show()
    return track, home_lines, finish, pawns


def game(screen, matrix):
    for line in range(len(matrix)):
        for c in range(len(matrix[line])):
            screen.print_at(matrix[line][c], line, c)
    while True:
        screen.refresh()
