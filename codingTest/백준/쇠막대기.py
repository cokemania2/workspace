# https://www.acmicpc.net/problem/10799
# 쇠막대기.py

stack = []
answer = 0
bar  = 0
before = ''
s = input()
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if stack[-1] == '(':
            stack.pop()
            if before == '(': #직전
                answer += len(stack)
            else:
                answer += 1
    before = i
print(answer)