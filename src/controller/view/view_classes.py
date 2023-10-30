import scrap_engine as se


class Base(se.Frame):
    def __init__(self, color: str, state: str = "float"):
        super().__init__(3, 5, corner_chars=("╔", "╗", "╚", "╝"), state=state)
        self.color = color
        self.pons = int()

    def add_pawn(self):
        self.pons += 1

    def add(self, screen: se.Map, x: int, y: int):
        super().add(screen, x, y)
        self.draw()