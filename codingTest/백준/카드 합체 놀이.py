# https://www.acmicpc.net/problem/15903
# 카드 합체 놀이.py

n, m = map(int, input().split())
cards = list(sorted(list(map(int,input().split()))))
for i in range(m):
    plus_num = cards[0] + cards[1]
    cards[0], cards[1] = plus_num, plus_num
    cards.sort()
print(sum(cards))
