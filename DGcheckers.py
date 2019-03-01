from graphics import *

print("Size of window?(500 recommended)");windowSize = int(input())
squareSize = (windowSize/10)
peiceSize = squareSize - (windowSize/17) 
checkersWin = GraphWin("Checkers", windowSize,windowSize);checkersWin.setCoords(0,0, windowSize,windowSize)

checkerBackground = Rectangle(Point(squareSize,squareSize),
                              Point(squareSize * 9,squareSize * 9))
checkerBackground.setFill(color_rgb(0,0,0));checkerBackground.draw(checkersWin)

for y in range(8):
    for x in range(8):
        checkerRect = Rectangle(Point(squareSize * (x + 1),squareSize * (y + 1)),
                                Point(squareSize * (x + 2),squareSize * (y + 2)))

        if ((y/2) % 1 == 0):
            if ((x/2) % 1 == 0) == False: checkerRect.setFill(color_rgb(230,30,30))
            else:
                if y < 3:
                    playerPiece = Circle(Point(squareSize * (1.5 + x),squareSize * (1.5 + y)),peiceSize)
                    playerPiece.setFill(color_rgb(230,50,50))
                    playerPiece.draw(checkersWin)
                elif y > 4:
                    playerPiece = Circle(Point(squareSize * (1.5 + x),squareSize * (1.5 + y)),peiceSize)
                    playerPiece.setFill(color_rgb(245,245,220))
                    playerPiece.draw(checkersWin)
        else:
            if ((x/2) % 1 == 0): checkerRect.setFill(color_rgb(230,30,30))
            else:
                 if y < 3:
                    playerPiece = Circle(Point(squareSize * (1.5 + x),squareSize * (1.5 + y)),peiceSize)
                    playerPiece.setFill(color_rgb(230,50,50))
                    playerPiece.draw(checkersWin)
                 elif y > 4:
                    playerPiece = Circle(Point(squareSize * (1.5 + x),squareSize * (1.5 + y)),peiceSize)
                    playerPiece.setFill(color_rgb(245,245,220))
                    playerPiece.draw(checkersWin)
        checkerRect.draw(checkersWin)

    
