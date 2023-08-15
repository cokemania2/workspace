from collections import Counter

def solution(k, tangerine):
    # 서로 다른 종류의 수를 최소화
    # 딕셔너리에 담아서 정렬
    gyul_box = Counter(tangerine)
    sorted_gyul_box = sorted(gyul_box.items(), key=lambda x:x[1], reverse=True)

    for i, box in enumerate(sorted_gyul_box):
        k -= box[1]
        if k <= 0:
            return i + 1
    return len(gyul_box)