# https://www.acmicpc.net/problem/14916

answer = 0
flag = True
n = int(input())
while n % 5 != 0 :
    if n == 1 :
        flag = False
        print(-1)
        break
    n -= 2
    answer += 1
answer += n // 5
if flag :
    print(answer)
