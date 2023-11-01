import scrap_engine as se
from termcolor import colored


class Base(se.Frame):
    def __init__(self, color: int, state: str = "float"):
        corner = get_colored(color, "+")
        hchar = get_colored(color, "-")
        vchar = get_colored(color, "|")

        super().__init__(5, 7, corner_chars=(corner, corner, corner, corner),
                         horizontal_chars=(hchar, hchar), vertical_chars=(vchar, vchar),
                         state=state)

    # def add_pawn(self):
    #     self.pons += 1
    #
    # def add(self, screen: se.Map, x: int, y: int):
    #     super().add(screen, x, y)
    #     self.draw()


class HomeLineTile(se.Frame):
    def __init__(self, color: int, state: str = "float"):
        star = get_colored(color, "*")
        super().__init__(3, 5, corner_chars=(star, star, star, star),
                         horizontal_chars=(star, star), vertical_chars=(star, star),
                         state=state)


class Pawn(se.Object):
    def __init__(self, color: int):
        super().__init__(get_colored(color, "@"))
        self.color = color
        self.cursor = False
    def CursorSwitch(self):
        if self.cursor:
            self.cursor = False
            self.rechar(get_colored(self.color, "@"))
        else:
            self.cursor = True
            self.rechar(get_colored(self.color, "@", "on_light_grey"))



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
