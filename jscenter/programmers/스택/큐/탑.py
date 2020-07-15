def solution(heights):
    answer = []
    for i in range (len(heights)-1,0,-1) :
        flag = False
        for j in range (i-1,-1,-1) :
            if (heights[j] > heights[i] ) :
                answer.append(j+1)
                flag = True
                break
        if (flag == False ) :
            answer.append(0)
    answer.append(0)
    answer.reverse()
    return answer

print(solution([5, 4, 3, 2, 1 ]))
