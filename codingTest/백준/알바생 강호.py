# https://www.acmicpc.net/problem/1758
# 알바생 강호.py

def countTip(tip, order):
    tip -= (order -1)
    return tip if tip >= 0 else 0

answer = 0
customer = []
n = int(input())
for i in range(n):
    customer.append(int(input()))
customer.sort(reverse=True)
for i,v in enumerate(customer):
    answer += countTip(v, i + 1)
print(answer)
