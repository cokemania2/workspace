# https://www.acmicpc.net/problem/1181
# 단어 정렬.py

import sys

N = int(input())
word = []
before = ''
for i in range(N):
    word.append(sys.stdin.readline().split()[0])
for i in list(sorted(word, key = lambda x : (len(x), x))):
    if i != before:
        print(i)
        before = i