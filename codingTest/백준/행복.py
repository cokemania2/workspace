##https://www.acmicpc.net/problem/15969
##행복

n = int(input())
nlist = list(map(int, input().split(' ')))
print(max(nlist) - min(nlist))
