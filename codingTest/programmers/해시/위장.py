def solution(clothes):
    answer = 1
    dic = {}
    cnt = 0;

    for i in range (len(clothes)) :
        if (clothes[i][1] in dic) :
            dic[clothes[i][1]] = dic.get(clothes[i][1]) + 1
        else :
            dic[clothes[i][1]] = 2
    for i in dic.values() :
        answer = answer * i
    return answer - 1

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))
