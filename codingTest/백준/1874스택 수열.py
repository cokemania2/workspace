import sys
N = int(sys.stdin.readline())
index = 0
answer = ''
for i in range (N) :
    a = int(sys.stdin.readline())
    if ( a > index ) :
        answer = answer + '+\n'*(a-index) + '-\n'
        index = a
    else :
        if (a > before ) :
            answer = 'NO'
            break
        answer = answer + '-\n'
    before = a
print(answer)
