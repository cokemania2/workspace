##https://www.acmicpc.net/problem/17094
##Serious Problem

n = int(input())
s = input()

if s.count('2') > s.count('e') :
    print('2')
elif s.count('e') > s.count('2') :
    print('e')
else:
    print('yee')
