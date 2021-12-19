# 팰린드롬 만들기.py
# https://www.acmicpc.net/problem/1254

n = input()
n2 = n[::-1]
s = ""
for i,v in enumerate(n):
    if n+s[::-1] ==  s + n2:
       print(i + len(n))
       break
    s = s + v