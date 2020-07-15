def solution(progresses, speeds):
    answer = []
    stack = 0
    day = 0
    i = 0
    while(True) :
        if ( i == len(speeds)) :
            break
        print(progresses[i],i,stack,day)
        if (progresses[i] + speeds[i]*day >= 100 ) :     
            stack = stack + 1
            i = i + 1
        else :
            res = (100 - (progresses[i] + speeds[i]*day))//speeds[i]
            if (100 - progresses[i] + speeds[i]*day) % speeds[i] != 0 :
                res = res + 1
            day = day + res
            if ( stack != 0 ) :
                answer.append(stack)
                stack = 0
                
    answer.append(stack)
    return answer
print(solution([5,4,3,2,1],[1,1,1,1,1]))
