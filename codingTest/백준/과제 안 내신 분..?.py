# https://www.acmicpc.net/problem/5597
# 과제 안 내신 분..?

s = [False for _ in range(30)] 
for i in range(28):
    s[int(input())-1] = True
for i,v in enumerate(s):
    if v == False:
        print(i+1)
