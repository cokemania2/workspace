# https://www.acmicpc.net/problem/1076
# 저항.py

dic = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
a = dic[input()]
b = dic[input()]
c = dic[input()]
print(int(a*10+b)*(10**c))