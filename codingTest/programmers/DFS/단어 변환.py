# https://programmers.co.kr/learn/courses/30/lessons/43163
# 단어 변환.py

def DFS(depth, pivot, target, words, index):
    answer = []
    if pivot == target:
        return depth
    else:
        for i,v in enumerate(words):
            if is_one_diff(pivot, v) and index[i]:
                index[i] = False
                d = DFS(depth + 1, v, target, words, index)
                if d is not None:
                    answer.append(d)
                index[i] = True
    if len(answer) != 0:
        return min(answer)

def is_one_diff(word1, word2):
    diff = 0 
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    return True if diff == 1 else False

def solution(begin, target, words):
    index = [True for _ in range(len(words))]
    d = DFS(0, begin, target, words, index)
    return d if d is not None else 0