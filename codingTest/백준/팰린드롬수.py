# https://www.acmicpc.net/problem/1259
# 팰린드롬수.py

while True:
    n = input()
    if n == '0':
        break
    print('yes') if n == n[::-1] else print('no')