import datetime as dt
A, B = map(int, input().split())
C = int(input())
now = dt.datetime(2021, 8, 29, A, B)
af = dt.timedelta(minutes=C)
afdt = now + af
print(afdt.hour, afdt.minute)