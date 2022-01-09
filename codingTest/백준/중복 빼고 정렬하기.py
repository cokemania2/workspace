# https://www.acmicpc.net/problem/10867
# 중복 빼고 정렬하기.py

N = int(input())
n_list = list(sorted(list(set(map(int,input().split())))))
for i in n_list:
    print(i,end=' ')