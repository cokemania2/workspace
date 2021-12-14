# https://www.acmicpc.net/submit/2495/36318482
# 연속구간.py

for i in range(3):
    cnt = 1
    maxx = 1
    tmp = ""
    s = input()
    for i in s:
        if tmp == i:
            cnt += 1
        else:
            cnt = 1
        if cnt > maxx:
            maxx =  cnt
        tmp = i
    print(maxx)
