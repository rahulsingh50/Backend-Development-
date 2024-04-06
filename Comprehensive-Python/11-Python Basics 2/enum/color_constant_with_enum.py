from enum import Enum


class Color(Enum):
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'


# color = Color.RED

def check_color(color: Color):
    if color == Color.RED:
        print("Color is RED")
    elif color == Color.BLUE:
        print("Color is Blue")
    elif color == Color.GREEN:
        print("Color is Green")


check_color(Color.BLUE)

