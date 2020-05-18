import time
from tkinter import *
import random

boardStartPoint = (0, 0)
boardEndPoint = (500, 500)
squareSize = (boardEndPoint[0]-boardStartPoint[0])/9
finishedSquares=0
g=3
data=[]
for _ in range(9):
    a = []
    for _ in range(9):
        a.append(0)
    data.append(a)

possible=[]
for _ in range(9):
    a = []
    for _ in range(9):
        a.append([])
    possible.append(a)

board = [
    [7,0,0,4,0,0,1,2,0],
    [0,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,0],
    [0,0,7,0,4,0,0,6,0],
    [0,0,1,0,0,0,9,3,0],
    [9,0,4,0,0,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,0,9,2,1,6,8,5,7]
]

def drawBoard():
    for i in range(10):
        w=3 if i%3==0 else 1
        canvas.create_line(i*squareSize+g,0+g,i*squareSize+g,9*squareSize+g, width=w)
        canvas.create_line(0+g,i*squareSize+g,9*squareSize+g,i*squareSize+g, width=w)

def put(x,y,num,color="black"):
    h=int(g+squareSize/2)
    canvas.create_text(x*squareSize+h,y*squareSize+h, text=str(num), font=("",int(squareSize/1.5)), fill=color)
    data[x][y] = num
    global finishedSquares
    finishedSquares += 1
    if color!="black":
        # root.update()
        # time.sleep(1/10)
        pass

def getPossible():
    pos=[[[] for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if data[i][j] != 0:
                continue
            col = data[i]
            row = [t[j] for t in data]
            pos[i][j] = []
            for number in range(1, 10):
                if number in col or number in row:
                    pass
                else:
                    found = False
                    for ti in range(3 * (i // 3), 3 * (i // 3) + 3):
                        for tj in range(3 * (j // 3), 3 * (j // 3) + 3):
                            if number == data[ti][tj]:
                                found = True
                                # print("found " + str(number) + " in " + str((ti, tj)))
                    if not found:
                        pos[i][j].append(number)
    return pos


def doTrivials():
    global possible
    for i in range(9):
        for j in range(9):
            if data[i][j] != 0:
                continue
            col = data[i]
            row = [t[j] for t in data]
            possible[i][j] = []
            for number in range(1, 10):
                if number in col or number in row:
                    pass
                else:
                    found = False
                    for ti in range(3 * (i // 3), 3 * (i // 3) + 3):
                        for tj in range(3 * (j // 3), 3 * (j // 3) + 3):
                            if number == data[ti][tj]:
                                found = True
                                # print("found " + str(number) + " in " + str((ti, tj)))
                    if not found:
                        possible[i][j].append(number)
            if len(possible[i][j]) == 1:
                put(i, j, possible[i][j][0], "red")


def getMinPos(pos):
    ar=[]
    for i in range(9):
        a=[]
        for j in range(9):
            a.append(len(pos[i][j]))
        ar.append(a)
    min = 1000
    mindex = 0, 0
    for i in range(9):
        for j in range(9):
            if ar[i][j] != 0 and ar[i][j] < min:
                mindex = i, j
                min = ar[i][j]
                if min == 1:
                    return mindex
    return mindex


def solve():
    while finishedSquares < 81:
        startFinished = finishedSquares
        doTrivials()
        if finishedSquares == startFinished:
            tempfinishedSquares = finishedSquares
            tempPos = getPossible()
            i, j = getMinPos(tempPos)
            tempData = data.copy()
            num = tempPos[i][j][0]
            tempData[i][j] = num

            break
            # pass
        print(finishedSquares)


if __name__ == '__main__':
    root = Tk()
    root.geometry("{}x{}".format(600,600))
    # root.bind('<Configure>', resize)

    canvas = Canvas(root)
    canvas.configure(width=squareSize*10,height=squareSize*10)
    drawBoard()

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                put(j, i, board[i][j])

    canvas.place(x=50,y=50)
    root.after(0,solve)
    root.mainloop()
