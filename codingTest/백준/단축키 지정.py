# https://www.acmicpc.net/problem/1283
# 단축키 지정.py

def check_string(s, dic):
    for i, v in enumerate(s):
        v = v.upper()
        if v not in dic:
            dic[v] = True
            return (True, i)
    return (False, 0)

def check_head(s, dic):
    for i,v in enumerate(s.split()):
        head = v[0].upper()
        if head not in dic:
            dic[head] = True
            return (True, i)
    return (False, 0)

def print_head(s, index):
    answer = ""
    for i, v in enumerate(s.split()):
        if i == index:
            answer += "[" + v[0] + "]" + v[1:] + " "
        else:
            answer += v + " "
    print(answer, end='')

def print_all(s, index):
    answer = ""
    for i, v in enumerate(list(s)):
        if i == index:
            answer += "[" + v[0] + "]" + v[1:]
        else:
            answer += v
    print(answer, end=' ')    

dic = {}
n = int(input())
for i in range(n):
    command = input()
    ok , index = check_head(command, dic)
    if ok:
        print_head(command, index)
    else:
        flag = False
        for s in command.split():
            if not flag:
                ok, index = check_string(s, dic)
                if ok:
                    print_all(s,index)
                    flag = True
                    continue
            print(s,end=' ')
    print()

