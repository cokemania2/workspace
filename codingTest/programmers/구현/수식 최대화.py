import re
from itertools import permutations

def solution(expression):
    
    
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    arr = re.findall('\d+|[*+-]',expression)
    print(arr)
    answer = []
    for x in op :
        copyx = arr[:]
        for y in x :
            while y in copyx :
                tmp = copyx.index(y)
                copyx[tmp - 1] = str(eval(copyx[tmp-1]+copyx[tmp]+copyx[tmp+1]))
                copyx = copyx[:tmp] + copyx[tmp+2:]
        answer.append(copyx[-1])
        
    return max(abs(int(x)) for x in answer)
print(solution("100-200*300-500+20"))


import re
from itertools import permutations

def solution2(expression):
    answer = 0
    arr = re.findall('\d+|[*+-]',expression)
    op = [x for x in  ['*','+','-'] if x in expression]
    op2 = [list(y) for y in permutations(op)]
    for i in op2 :
        copyarr = arr[:]
        for j in i :
            while j in copyarr :
                index = copyarr.index(j)
                tmp = eval(str(copyarr[index-1]) + copyarr[index] + str(copyarr[index + 1]))
                copyarr[index-1] = tmp
                del copyarr[index:index+2]
        if abs(copyarr[0]) > answer :
            answer = abs(copyarr[0])
                
    return answer