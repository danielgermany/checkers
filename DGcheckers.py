from graphics import *
from math import isclose

boardSize = 10

def is_whole(n):
    if n % 1 == 0:
        return True
    else:
        return False

checkersWin = GraphWin("Checkers", 600,600)
checkersWin.setCoords(0,0, 1000,1000)

for x in range(boardSize):
 
    if is_whole(x/2) or x == 0:
        checkerRect = Rectangle(Point(750 + (50 * x),750),Point(700 + (50 * x),700))
        checkerRect.setFill(color_rgb(230,30,30))
        checkerRect.draw(checkersWin)
    else:
        checkerRect = Rectangle(Point(750 + (50 * x),750),Point(700 + (50 * x),700))
        checkerRect.setFill(color_rgb(0,0,0))
        checkerRect.draw(checkersWin)
