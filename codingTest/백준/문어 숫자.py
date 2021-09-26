# https://www.acmicpc.net/problem/1864
# 문어 숫자.py

dic ={'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1}
while True:
    answer = 0
    minus = 1
    n = input()
    if n == '#':
        break
    for i in range(len(n)):
        if minus == -1:
            minus = 1
            continue
        if dic[n[len(n)-i -2]] == '/':
            minus = -1
        answer += dic[n[len(n) - i - 1]] * 8 **  i * minus
    print(answer)
