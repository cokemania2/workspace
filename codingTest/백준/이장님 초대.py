# https://www.acmicpc.net/problem/9237
# 이장님 초대.py

N = int(input())
myo = sorted(list(map(int,input().split())),reverse=True)
for i,v in enumerate(myo):
    myo[i] += i + 1 # 날짜 더해줌
print(max(myo)+ 1)
