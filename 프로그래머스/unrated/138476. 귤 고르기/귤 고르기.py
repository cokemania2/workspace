def solution(k, tangerine):
    answer = 0 
    # 서로 다른 종류의 수를 최소화
    # 딕셔너리에 담아서 정렬
    gyul_box = dict()
    for t in tangerine:
        if t in gyul_box:
            gyul_box[t] += 1
        else:
            gyul_box[t] = 1
    sorted_gyul_box = sorted(gyul_box.items(),key=lambda x:x[1],reverse=True)
    for i, box in enumerate(sorted_gyul_box):
        k -= box[1]
        if k <= 0:
            return i + 1
    return len(gyul_box)