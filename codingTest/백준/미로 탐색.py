# https://www.acmicpc.net/problem/2178
# 미로 탐색.py
import copy
import sys

def dfs(y, x, maze, step):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    global answer, N, M
    if step >= answer:
        return
    if y == N-1 and x == M-1:
        answer = step
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < M and ny < N and nx >= 0 and ny >=0 and maze[ny][nx] == '1':
            copy_maze = copy.deepcopy(maze)
            copy_maze[ny][nx] = 0
            dfs(ny, nx, copy_maze, step + 1)
            copy_maze[ny][nx] = 1

answer = sys.maxsize
maze = []
N, M = map(int, (input().split()))
for i in range(N):
    maze.append(list(input()))
dfs(0, 0, maze, 1)
print(answer)