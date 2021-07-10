# https://www.acmicpc.net/problem/1264

alpha = [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True :
    count = 0
    s = list(input())
    if s[0] == '#' :
        break
    for i in alpha :
        count += s.count(i)
    print(count)