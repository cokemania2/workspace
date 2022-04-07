# https://programmers.co.kr/learn/courses/30/lessons/12905
# 가장 큰 정사각형 찾기.py

def solution(board):
    maxx = 0
    if (len(board) == 1 or len(board[0]) == 1) :
        return 1
    for i in range(1,len(board)) :
        for j in range(1,len(board[0])) :
            if (board[i][j] == 1) :
                board[i][j] = min(min(board[i-1][j],board[i][j-1]),board[i-1][j-1]) + 1
                if ( board[i][j] > maxx ) :
                    maxx = board[i][j]
    return maxx * maxx