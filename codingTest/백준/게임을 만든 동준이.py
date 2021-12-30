# acmicpc.net/problem/2847
# 게임을 만든 동준이.py

answer = 0
N = int(input())
score_list = list(reversed([int(input()) for i in range(N)]))
for i in range(1, N):
    if score_list[i] >= score_list[i-1]:
        answer += score_list[i] - score_list[i-1] + 1
        score_list[i] = score_list[i-1] - 1
print(answer)


