from collections import deque

def nextXY(n, maps, sizeY, sizeX) :
    y = n[0]
    x = n[1]
    depth = n[2]
    nextque = []
    if y - 1>= 0 and maps[y - 1][x] != 0 : #up
        nextque.append([y - 1, x, depth + 1])
    if y + 1 < sizeY and maps[y + 1][x] != 0 : #down
        nextque.append([y + 1, x, depth + 1])
    if x + 1 < sizeX and maps[y][x + 1] != 0 : #right
        nextque.append([y, x + 1, depth + 1])
    if x - 1 >= 0 and maps[y][x - 1] != 0  : #left
        nextque.append([y, x - 1, depth + 1])
    return nextque

def isFinish(y, x, sizeY, sizeX) :
    if y == sizeY -1  and x == sizeX - 1 :
        return True
    else :
        return False

def solution(maps):
    queue = deque([[0,0,1]])
    sizeY = len(maps)
    sizeX = len(maps[0])
    while queue :
        n = queue.popleft()
        if maps[n[0]][n[1]] != 0 :
            if isFinish(n[0], n[1], sizeY, sizeX) :
                return n[2]
            maps[n[0]][n[1]] = 0
            queue +=  nextXY(n, maps, sizeY, sizeX)
    return -1