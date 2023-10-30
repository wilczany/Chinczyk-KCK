# from src.controller.view.menu import App
from src.controller.view.view import drawBoard
from src.controller.view.view import game
import scrap_engine as se

from curses import wrapper

if __name__ == "__main__":
    # mymap = se.Map(background=" ")  # defines mymap as a map as big as the terminal window with the background " "
    # mytext = se.Text("Hello world")  # defines a text as "Hello world"
    # myrectangle = se.Square(height=5, width=6,
    #                         char="#")  # defines a rectangle width height 5, width 6 and the character "#"
    # myframe = se.Frame(height=7, width=8, corner_chars=["┌", "┐", "└", "┘"], horizontal_chars=["─", "─"],
    #                    vertical_chars=["│", "│"])  # defines a frame see scrap_engine.Frame
    #
    # mytext.add(mymap, 0, 0)  # adds mytext to (0|0)
    # myrectangle.add(mymap, 2, 2)  # adds myrectangle to (2|2)
    # myframe.add(mymap, 1, 1)  # adds myframe to (1|1)

    #mymap.show()  # now a frame with a rectangle and a text above it should be shown
    
    drawBoard(2)
