from collections import Counter

def choice_one(a, b, counter):
    return a if counter[a] >= counter[b] else b

def make_type(counter):
    type = ""
    type += choice_one('R', 'T', counter)
    type += choice_one('C', 'F', counter)
    type += choice_one('J', 'M', counter)
    type += choice_one('A', 'N', counter)
    return type

def solution(survey, choices):
    counter = Counter(['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'])
    for i, v in enumerate(survey):
        left, right = 8 - choices[i], choices[i]
        counter[v[0]] += left
        counter[v[1]] += right
    return make_type(counter)
