# https://www.acmicpc.net/problem/17413
# 단어 뒤집기 2.py

stack = []
answer = ""
substr = ""
s = input()
for i in s:
    if i == '<':
        stack.append(i)
        answer += substr + i
        substr = ''
    elif i == '>':
        stack.pop()
        answer += i
    else:
        if len(stack) != 0:
            answer += i
        else:
            if i != ' ':
                substr = i + substr
            else:
                answer += substr + i
                substr = ''
if substr != '':
    answer += substr
print(answer)
