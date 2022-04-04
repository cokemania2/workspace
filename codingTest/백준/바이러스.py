# https://www.acmicpc.net/problem/2606
# 바이러스.py

def dfs(dic, n, index_map):
    for i in set(dic[n]):
        if i not in index_map:
            index_map[i] = True
            index_map = dfs(dic, i, index_map)
    return index_map

def insert(a, b, dic):
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]

index_map = {}
dic = {}
computer = int(input())
couple = int(input())
for _ in range(couple):
    c = input().split()
    insert(c[0], c[1], dic)
    insert(c[1], c[0], dic)

index_map = dfs(dic, '1', index_map)
print(len(index_map.keys()))


