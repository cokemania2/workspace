# https://programmers.co.kr/learn/courses/30/lessons/42883
# 큰 수 만들기.py


def solution(number, k):
    answer = ''
    stack = []
    i = 0
    while True:
        if i == len(number):
            break
        if k == 0 or len(stack) == 0:
            stack.append(number[i])
        elif stack[-1] <  number[i]:
            stack.pop()
            i -= 1
            k -= 1
        else:
            stack.append(number[i])
        i += 1
    if k == 0:
        print(1)
        return "".join(stack)
    while True:
        for i in range(0, 10):
            for j in range(len(stack)):
                if int(stack[j]) == i:
                    stack[j] = ""
                    k -= 1
                    if k == 0:
                        return "".join(stack)