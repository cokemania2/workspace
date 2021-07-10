# https://www.acmicpc.net/problem/14920

n = int(input())
cnt = 1
while n != 1 :
    cnt += 1
    if n % 2 == 0 :
        n /= 2
    else :
        n = n * 3 + 1
print(cnt)