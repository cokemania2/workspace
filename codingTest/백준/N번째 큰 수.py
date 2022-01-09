# N번째 큰 수.py
# https://www.acmicpc.net/problem/2693

T = int(input())
for i in range(T):
    print(list(sorted(list(map(int,input().split()))))[-3])