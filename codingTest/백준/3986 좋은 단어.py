#스택, 문자열 나누기

import sys
N = int(sys.stdin.readline().rstrip())
answer =0
for i in range (N) :
    stack =[]
    a = list(input())
    for j in range (len(a)) :
        if (len(stack) == 0) :
            stack.append(a[j])
        elif ( a[j] == 'A') :
            if (stack[-1] == 'A') :
                stack.pop()
            else :
                stack.append('A')
        elif ( a[j] == 'B') :
            if (stack[-1] == 'B') :
                stack.pop()
            else :
                stack.append('B')
    if (len(stack) == 0 ) :
        answer = answer +1
print(answer)
