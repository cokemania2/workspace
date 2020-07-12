from functools import cmp_to_key

def solution(arrangement):
    answer = 0
    bar = 0
    for i in range (len(arrangement)) :
        if (arrangement[i] == '(') :
           bar = bar + 1
        else :
            if (arrangement[i-1] == '(') :
                bar = bar -1
                answer = answer + bar
            else :
                bar = bar - 1
                answer = answer + 1
    return answer

##def solution(arrangement):
##    answer = 0
##    sticks = 0
##    rasor_to_zero = arrangement.replace('()','0')
##
##    for i in rasor_to_zero:
##        if i == '(':
##            sticks += 1
##        elif i =='0' :
##            answer += sticks
##        else :
##            sticks -= 1
##            answer += 1
##
##    return answer
print(solution("()(((()())(())()))(())"))
                 
