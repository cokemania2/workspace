# https://programmers.co.kr/learn/courses/30/lessons/17679?language=python3
# 프랜즈4블록.py

def find_pop(m, n, board):
    find_set = set()
    for y in range(n-1):
        for x in range(m-1):
            if (board[y][x] == board[y][x+1] == 
                board[y+1][x] == board[y+1][x+1] != '_'):
                find_set |= set([(y,x),(y,x+1),(y+1,x),(y+1,x+1)])
    for y, x in find_set:
        board[y][x] = '0'
    for y in range(n):
        board[y] = (['_' for i in range(board[y].count('0'))]
            + [z for z in board[y] if z != '0'])
    return len(find_set)
                
def solution(m, n, board):
    answer = 0
    
    b = list(map(list,zip(*board)))
    while True:
        x = find_pop(m,n,b)
        if x == 0:
            return answer
        else:
            answer += x