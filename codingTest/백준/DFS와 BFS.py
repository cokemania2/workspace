# https://www.acmicpc.net/problem/1260
# DFS와 BFS.py


def insert(dic, key, value):
    if key in dic:
        dic[key].append(value)
    else:
        dic[key] = [value]
    return dic

def dfs(dic, key):
    global answer_dfs
    if key in dic and key not in answer_dfs:
        answer_dfs.append(key)
        for i in sorted(dic[key]):
            dfs(dic, i)

def bfs(dic, queue):
    global answer_bfs
    if len(queue) == 0:
        return
    key = queue.pop(0)
    if key in dic and key not in answer_bfs:
        answer_bfs.append(key)
        for i in sorted(dic[key]):
            queue.append(i)
    bfs(dic, queue)
    

answer_dfs = []
answer_bfs = []
dic = {}


N, M, V = map(int, input().split())
for i in range(M):
    a, b = map(int, input().split())
    dic = insert(dic, a, b)
    dic = insert(dic, b, a)
dfs(dic, V)
bfs(dic, [V])
for i in answer_dfs:
    print(i, end= ' ')
print()
for i in answer_bfs:
    print(i, end= ' ')
