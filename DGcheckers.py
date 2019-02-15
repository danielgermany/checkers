from graphics import *

boardSize = 10

checkersWin = GraphWin("Checkers", 600,600)
checkersWin.setCoords(0,0, 1000,1000)

for x in range(boardSize):
    checkerRect = Rectangle(Point(750 + (50 * x),750),Point(700 + (50 * x),700))
    checkerRect.setFill(color_rgb(230,30,30))
    checkerRect.draw(checkersWin)
    
