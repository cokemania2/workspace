# https://www.acmicpc.net/problem/7600
# 문자가 몇갤까 

# 중복되는 문자를 피해서 count 해준다.

while True :
    alpha = 0
    dic = {}
    s = list(input().upper())
    if len(s) == 1 and s[0] == '#' :
        break
    for i in s :
        if i >= 'A' and i <= 'Z' and i not in dic :
            alpha += 1
            dic[i] = True
    print(alpha)
