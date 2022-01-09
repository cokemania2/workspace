# 두 수의 합.py
# https://www.acmicpc.net/problem/3273

n = int(input())
n_list = list(sorted(list(map(int,input().split()))))
k = int(input())
answer = 0 
left = 0
right = n - 1
while True:
    if left < 0 or right >= n or left >= right:
        break
    v = n_list[left] + n_list[right]
    if v == k:
        answer += 1
        left += 1
        right -= 1
    elif v > k:
        right -= 1
    else:
        left += 1
print(answer)
