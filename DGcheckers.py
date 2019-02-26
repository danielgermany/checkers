from graphics import *
from DGcheckersFunc import is_whole

print("Size of window?")
windowSize = int(input())

checkersWin = GraphWin("Checkers", windowSize,windowSize)
checkersWin.setCoords(0,0, windowSize,windowSize)

for y in range(8):
    for x in range(8):

        checkerRect = Rectangle(Point((windowSize/10) * (x + 1),(windowSize/10) * (y + 1)),
                                Point((windowSize/10) * (x + 2),(windowSize/10) * (y + 2)))
        if is_whole(y/2):
            if is_whole(x/2): checkerRect.setFill(color_rgb(230,30,30))
            else: checkerRect.setFill(color_rgb(0,0,0))
        else:
            if is_whole(x/2): checkerRect.setFill(color_rgb(0,0,0))
            else: checkerRect.setFill(color_rgb(230,30,30))

        checkerRect.draw(checkersWin)
