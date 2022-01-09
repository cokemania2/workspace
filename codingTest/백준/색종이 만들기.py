# https://www.acmicpc.net/problem/2630
# 색종이 만들기.py

def divide_and_conquer(a,b,c,d,n_list):
    global result
    for i in range(a,b):
        for j in range(c,d-1):
            if n_list[i][j] != n_list[i][j+1]:
                divide_and_conquer(a, b//2, c, d//2, n_list)
                divide_and_conquer(a, b//2, d//2, d, n_list)
                divide_and_conquer(b//2, b, c, d//2, n_list)
                divide_and_conquer(b//2, b, d//2, d, n_list)
                return
    result.append(n_list[a][b])

result = []
n_list = []
n = int(input())
for i in range(n):
    n_list.append(input().split())

divide_and_conquer(0,n,0,n,n_list)
print(result)

