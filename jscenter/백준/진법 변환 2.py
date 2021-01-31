# https://www.acmicpc.net/problem/11005

# 아스키코드를 활용했다.
# 0 ~ 9 = 48 ~ 57
# A ~ Z = 65 ~ 90


answer = []
flag = False
N, B = map(int,input().split())
while True :
    if N % B == N :
        flag = True
    if N % B < 10 :
        answer += chr(ord('0') + N % B)
    else :
        answer += chr(ord('A') + (N % B - 10))
    N //= B
    if flag :
        break
print(''.join(reversed(answer)))
