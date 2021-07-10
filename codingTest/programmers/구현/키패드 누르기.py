import math

def distance(a,b) :
    return ((abs(a) + abs(b)))

def solution(numbers, hand):
    answer = ''
    ltmp = 9
    rtmp = 11
    LD = 0
    RD = 0
    x = 0
    y = 0

    for i in range (len(numbers)) :
        if (numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7) :
            answer = answer + 'L'
            ltmp = numbers[i] - 1
        elif (numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9) :
            answer = answer + 'R' 
            rtmp = numbers[i] - 1
        else :
            if (numbers[i] == 0) :
                numbers[i] = 10
            else :
                numbers[i] = numbers[i] - 1
            y = numbers[i] // 3
            x = numbers[i] % 3
            LD = distance(y - (ltmp // 3) , x - (ltmp % 3))
            RD = distance(y - (rtmp // 3) , x - (rtmp % 3))
            if ( LD < RD ) :
                answer = answer + 'L'
                ltmp = numbers[i]
            elif ( LD > RD):
                answer = answer + 'R' 
                rtmp = numbers[i]
            else :
                if (hand == 'right') :
                    answer = answer + 'R' 
                    rtmp = numbers[i]
                else :
                    answer = answer + 'L'
                    ltmp = numbers[i]
        
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
