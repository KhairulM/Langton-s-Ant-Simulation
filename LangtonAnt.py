import cv2
import numpy as np
import random

class POINT:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ANT(POINT):
    def __init__(self, x, y, direction):
        self.pos = POINT(x, y)          # Relative to canvas/map
        self.dir = direction            # 0 - 3, 0=right, 1=up, 2=left, 3=down

    def move(self):
        if self.dir == 0:
            self.pos.x += 1
        elif self.dir == 1:
            self.pos.y -= 1
        elif self.dir == 2:
            self.pos.x -= 1
        else:
            self.pos.y +=1

    def update(self, left):
        if left:
            self.dir = (self.dir + 1) % 4
            self.move()
        else:
            self.dir = (self.dir - 1) % 4
            self.move()

def updtAnts(arrAnts, canvas):
    height, width = canvas.shape[:2]

    for ant in arrAnts:
        if (ant.pos.x >= width-1) or (ant.pos.x <= 0) or (ant.pos.y >= height-1) or (ant.pos.y <= 0):
                canvas[ant.pos.y][ant.pos.x] = (255, 255, 255)
                ant.update(True)
        elif np.any(canvas[ant.pos.y][ant.pos.x] != 0):
                canvas[ant.pos.y][ant.pos.x] = (0, 0, 0)
                ant.update(False)
        else:
                canvas[ant.pos.y][ant.pos.x] = (255, 255, 255)
                ant.update(True)

def drawAnts(arrAnts, canvas):
    for ant in arrAnts:
        oldColor = canvas[ant.pos.y][ant.pos.x]
        canvas[ant.pos.y][ant.pos.x] = (0, 0, 255)
        rez = cv2.resize(canvas, (500, 500), interpolation = cv2.INTER_AREA)
        cv2.imshow("Langton's Ant", rez)
        cv2.waitKey(1)
        canvas[ant.pos.y][ant.pos.x] = oldColor

def createAnts(arrAnts, canvas, nbAnts):
    height, width = canvas.shape[:2]

    for i in range(0, nbAnts):
        langton = ANT(random.randint(1, width-2), random.randint(1, height-2), random.randint(0, 3))            
        arrAnts.append(langton)          


def main():
    height = int(input("Height : "))
    width = int(input("Width : "))

    canvas = np.zeros((height, width, 3), np.uint8)
    canvas.fill(255)

    arrAnts = []
    nbAnts = int(input("Number of Ants : "))
    createAnts(arrAnts, canvas, nbAnts)

    while True:
        """
        print(langton.pos.x)
        print(langton.pos.y)
        print(langton.dir)
        """
        updtAnts(arrAnts, canvas)
        #drawAnts(arrAnts, canvas)

        rez = cv2.resize(canvas, (500, 500), interpolation = cv2.INTER_AREA)
        cv2.imshow("Langton's Ant", rez)
        cv2.waitKey(1)

main()