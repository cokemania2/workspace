# https://www.acmicpc.net/problem/2947
# 나무 조각.py

def print_a(a):
    for i in a:
        print(i,end=' ')
    print()

a = list(map(int,input().split()))
for i in range(1,len(a)):
    for j in range(len(a)-i):
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            print_a(a)
