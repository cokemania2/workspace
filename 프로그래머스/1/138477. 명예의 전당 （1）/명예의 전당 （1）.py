def solution(k, score):
    return [sorted(score[:x+1])[-k:][0] for x in range(len(score))]
