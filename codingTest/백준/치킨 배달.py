# https://www.acmicpc.net/problem/15686
# 치킨 배달.py

import itertools

def cal_distance(shop, home):
    return abs(home[0] - shop[0]) + abs(home[1] - shop[1])

N, M = map(int, input().split())
neighborhood = []
chicken_shop = []

home = []







for y in range(N):
    width = input().split()
    for x, v in enumerate(width):
        if v == '1':
            home.append([y,x])
        elif v == '2':
            chicken_shop.append([y,x])
distance_info = [[] for _ in range(len(home))]
for shop in chicken_shop:
    for i,h in enumerate(home):
        distance_info[i].append(cal_distance(shop, h))

arr = [i for i in range(len(chicken_shop))]
nPr = list(itertools.permutations(arr, M))
for i in nPr:
    for j in i:
        
# print(list(map(list, zip(*distance_info))))

# for i in range(M):
    
