from graphics import *
from math import isclose

boardSize = 20

def is_whole(n):
    if n % 1 == 0:
        return True
    else:
        return False

checkersWin = GraphWin("Checkers", 600,600)
checkersWin.setCoords(0,0, 1000,1000)

for y in range(boardSize):
    for x in range(boardSize):

        checkerRect = Rectangle(Point(0 + (50 * x),950 - (50 * y)),Point(100 + (50 * x),1000 - (50 * y)))

        if is_whole(y/2) or y == 0:
            if is_whole(x/2) or x == 0:
                checkerRect.setFill(color_rgb(230,30,30))
            else:
                checkerRect.setFill(color_rgb(0,0,0))
        else:
            if is_whole(x/2) or x == 0:
                checkerRect.setFill(color_rgb(0,0,0))
            else:
                checkerRect.setFill(color_rgb(230,30,30))
        checkerRect.draw(checkersWin)
