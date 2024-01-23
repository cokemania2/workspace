def solution(want, number, discount):
    answer = 0
    discount_dict = {}
    for w, n in zip(want, number):
        discount_dict[w] = n
    
    for i in range(len(discount)):
        for key, value in discount_dict.items():
            if discount[i:i+10].count(key) < value:
                break
        else:
            answer += 1
    return answer