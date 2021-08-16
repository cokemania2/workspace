# https://programmers.co.kr/learn/courses/30/lessons/83201
# 상호 평가.py

def checkToExclude(score, i):
    myScore = score[i]
    score = sorted(score)
    if (score[0] == myScore and score[1] != myScore or
        score[len(score)-1] == myScore and score[len(score)-2] != myScore):
            return True
    return False

def makeCredit(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'
    
def solution(scores):
    answer = ''
    length = len(scores)
    checkBoard = [True] * length
    scoreBoard = [[0]*length for _ in range(length)]
    for i, score in enumerate(scores):
        for j in range(length):
            scoreBoard[j][i] = score[j]
    for i, score in enumerate(scoreBoard):
        if checkToExclude(score,i):
            checkBoard[i] = False
            score[i] = 0
            
    for i in range(length):
        l = length
        if checkBoard[i] == False:
            l -= 1
        answer += makeCredit(sum(scoreBoard[i])//l)
        
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))