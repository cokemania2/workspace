# https://www.acmicpc.net/problem/2530
# 인공지능 시계.py

import datetime as dt

h, m , s= map(int, input().split())
plus_s = int(input())
d = dt.datetime(2021,8,8,h,m,s) + dt.timedelta(seconds=plus_s)
print(d.hour, d.minute, d.second)