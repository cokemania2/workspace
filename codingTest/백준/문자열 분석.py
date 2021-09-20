# https://www.acmicpc.net/submit/10820/33424416
# 문자열 분석.py

while True:
    try:
        countList = [0 for i in range(4)]
        s = input()
        for i in s:
            if i >= 'a' and i<= 'z':
                countList[0] += 1
            elif i >= 'A'  and i <= 'Z':
                countList[1] += 1
            elif i.isdigit():
                countList[2] += 1
            elif i.isspace():
                countList[3] += 1
        for i in countList:
            print(i, end=' ')
        print()
    except:
        break