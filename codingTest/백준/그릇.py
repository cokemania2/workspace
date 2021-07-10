cnt = 0
tmp = ''
v = list(input())
for i in v :
    if tmp == i :
        cnt += 5
    else :
        cnt += 10
    tmp = i
print(cnt)
