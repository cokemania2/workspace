def solution(bricks):
    answer = 0
    leftT = 0
    rightT = len(bricks) - 1

    for i, x in enumerate (bricks) :
        if (x >= bricks[leftT] and x != 0) :
            for j in range (leftT + 1,i) :
                answer += bricks[leftT] - bricks[j]
            leftT = i
    for i in range (len(bricks) -1 ,leftT -1,-1) :
        if (bricks[i] >= bricks[rightT] and bricks[i] != 0) :
            for j in range (i+1 , rightT) :
                answer += bricks[rightT] - bricks[j]
            rightT = i
    return answer