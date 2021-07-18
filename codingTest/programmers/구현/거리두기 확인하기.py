# 거리두기 확인하기.py
# https://programmers.co.kr/learn/courses/30/lessons/81302

def checkSafe(r, c, place) :
    if c + 1 < 5 and place[r][c + 1] == 'P':
        return False
    if r + 1 < 5 and place[r + 1][c] == 'P':
        return False
    if r + 1 < 5 and c + 1 < 5 and place[r+1][c+1] == 'P' :
        if place[r+1][c] != 'X' or place[r][c+1] != 'X' :
            return False
    if r - 1 >= 0 and c + 1 < 5 and place[r-1][c+1] == 'P' :
        if place[r-1][c] != 'X' or place[r][c+1] != 'X' :
            return False
    if c + 2 < 5 and place[r][c+2] == 'P' and place[r][c+1] != 'X':
        return False
    if r + 2 < 5 and place[r+2][c] == 'P' and place[r+1][c] != 'X':
        return False
    return True

def checkPlace(place) :
    for i in range(5) :
        for j in range(5) :
            if place[i][j] == 'P' and not checkSafe(i,j,place) :
                return False
    return True
    
def solution(places):
    answer = []
    for place in places :
        if checkPlace(place) :
            answer.append(1)
        else :
            answer.append(0)    
    return answer