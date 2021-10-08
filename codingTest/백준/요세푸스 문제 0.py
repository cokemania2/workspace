# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0.py

answer = []
N, K = map(int, input().split())
p = K - 1
q = [i for i in range(1, N+1)]
for i in range(len(q)):
    p %= len(q)
    answer.append(str(q[p]))
    q[:] = q[:p] + q[p+1:]
    p += K - 1
print('<'+', '.join(answer)+'>')