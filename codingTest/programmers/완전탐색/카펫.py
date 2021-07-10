def solution(brown, yellow):
    answer = []
    a = brown+yellow
    for i in range (3,a) :
        if (a%i == 0 ) :
            print(i,(i-2),(a//i-2))
            if (i-2)*(a//i-2) == yellow :
                return [a//i,i]
    return answer


print(solution(10,2))
