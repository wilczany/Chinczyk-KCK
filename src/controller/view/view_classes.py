import scrap_engine as se
from termcolor import colored


class Base(se.Frame):
    cords = [(2, 1), (2, 3), (4, 1), (4, 3)]

    def __init__(self, color: int, state: str = "float"):
        self.pawns = []
        self.pawns_count = 0

        corner = get_colored(color, "+")
        hchar = get_colored(color, "-")
        vchar = get_colored(color, "|")

        super().__init__(5, 7, corner_chars=(corner, corner, corner, corner),
                         horizontal_chars=(hchar, hchar), vertical_chars=(vchar, vchar),
                         state=state)

    def add_pawn(self, pawn):
        self.pawns.append(pawn)
        super().add_ob(pawn, self.cords[self.pawns_count][0], self.cords[self.pawns_count][1])
        self.pawns_count += 1

    def remove_pawn(self):
        self.pawns_count -= 1
        p = self.pawns.pop()
        super().rem_ob(p)
        p.remove()
        return p


class Tile(se.Frame):

    def __init__(self, color: int = None):
        self.pawn = None

        if color is None:
            super().__init__(3, 5, state="float")
        else:
            super().__init__(3, 5,
                             corner_chars=(get_colored(color, '+'), get_colored(color, '+'),
                                           get_colored(color, '+'), get_colored(color, '+')),
                             horizontal_chars=(get_colored(color, '-'), get_colored(color, '-')),
                             vertical_chars=(get_colored(color, '|'), get_colored(color, '|')),
                             )

    def add_pawn(self, pawn):
        self.pawn = pawn
        super().add_ob(pawn, 2, 1)
        self.pawn.redraw()

    def remove_pawn(self):
        tmp = self.pawn
        self.pawn = None
        super().rem_ob(tmp)
        tmp.remove()
        return tmp


class HomeLineTile(se.Frame):
    def __init__(self, color: int, state: str = "float"):
        star = get_colored(color, "*")
        super().__init__(3, 5, corner_chars=(star, star, star, star),
                         horizontal_chars=(star, star), vertical_chars=(star, star),
                         state=state)


class Pawn(se.Object):
    chars = {0: "G", 1: "B", 2: "R", 3: "Y"}

    def __init__(self, color: int, ):

        self.color = color
        self.cursor = False
        super().__init__(get_colored(color, self.chars[color]))

    def cursor_switch(self):
        if self.cursor:
            self.cursor = False
            self.rechar(get_colored(self.color, self.chars[self.color]))
        else:
            self.cursor = True
            self.rechar(get_colored(self.color, self.chars[self.color], "on_light_grey"))

        #self.redraw()

    def action(self, ob):
        pass


def get_colored(color: int, char: str, bg=None):
    match color:
        case 0:
            return colored(char, "green", bg)
        case 1:
            return colored(char, "magenta", bg)
        case 2:
            return colored(char, "red", bg)
        case 3:
            return colored(char, "yellow", bg)
