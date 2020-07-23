def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ai,bi,ci=0,0,0
    A,B,C=0,0,0
    for i in range (len(answers)) :
        if (answers[i] == a[ai]) :
            A = A + 1
        if (answers[i] == b[bi]) :
            B = B + 1    
        if (answers[i] == c[ci]) :
            C = C +1
        ai = ai + 1
        bi = bi + 1
        ci = ci + 1
        if (ai == len(a)) :
            ai = 0
        if (bi == len(b)) :
            bi = 0
        if (ci == len(c)) :
            ci = 0
    m = max(A,B,C)
    if (m == A) :
        answer.append(1)
    if (m == B) :
        answer.append(2)
    if (m == C) :
        answer.append(3)
    return answer
print(solution([1,3,2,4,2]))
c
+

