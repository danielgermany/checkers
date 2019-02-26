from graphics import *

print("Size of window?")
windowSize = int(input())

checkersWin = GraphWin("Checkers", windowSize,windowSize)
checkersWin.setCoords(0,0, windowSize,windowSize)

checkerBackground = Rectangle(Point(windowSize/10,windowSize/10),
                              Point((windowSize/10)*9,(windowSize/10)*9))
checkerBackground.setFill(color_rgb(0,0,0))
checkerBackground.draw(checkersWin)

for y in range(8):
    for x in range(8):
        checkerRect = Rectangle(Point((windowSize/10) * (x + 1),(windowSize/10) * (y + 1)),
                                Point((windowSize/10) * (x + 2),(windowSize/10) * (y + 2)))
 
        if ((y/2) % 1 == 0):
            if ((x/2) % 1 == 0): checkerRect.setFill(color_rgb(230,30,30))
        else:
            if ((x/2) % 1 == 0) == False: checkerRect.setFill(color_rgb(230,30,30))
        checkerRect.draw(checkersWin)
