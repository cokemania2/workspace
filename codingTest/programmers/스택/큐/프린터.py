def solution(priorities, location):
    answer = 0
    
    a = [0]*len(priorities)
    a[location] = 1
    b = list(zip(priorities,a))
    c = [0]*10
    tmp = 0
    for i in range (len(b)) :
        c[b[i][0]] = c[b[i][0]] + 1
    while( len(b) != 0 ) :
        flag = True
        for i in range (b[0][0]+1,10) :
            if (c[i] != 0 ) :
                tmp = b.pop(0)
                b.append(tmp)
                flag = False
                break
        if ( flag == True ) :
            answer = answer + 1
            if (b[0][1] == 1) :
                break
            c[b[0][0]] = c[b[0][0]] - 1
            b.pop(0)
    return answer

print(solution([2, 1, 3, 2],2))
                 
