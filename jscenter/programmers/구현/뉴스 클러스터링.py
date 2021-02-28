# 뉴스 클러스터링 
# https://programmers.co.kr/learn/courses/30/lessons/17677

# 영문자를 순서대로 두 글자씩 조합해서 얼마나 비슷한지 자카드 유사도를 검사하는 문제 이다.
# 중복된 문자가 있을 수 있으므로 딕셔너리를 이용해서 숫자를 높였다. 

def solution(str1, str2):
    answer = 0
    s1 = {}
    s2 = {}
    Intersection = {}
    Union  = {}
    a1 = 0
    a2 = 0
    for i in range(len(str1)) :
        tmp = str1[i:i+2].upper()
        if len(tmp) == 2 and tmp.isalpha() :
            if tmp in s1 :
                s1[tmp] = s1[tmp] + 1
            else :
                s1[tmp] = 1
    for i in range(len(str2)) :
        tmp = str2[i:i+2].upper()
        if len(tmp) == 2 and tmp.isalpha() :
            if tmp in s2 :
                s2[tmp] = s2[tmp] + 1
            else :
                s2[tmp] = 1
    Union = s1.copy()
    for i in s2 :
        if i in s1 :
            Intersection[i] = min(s1[i], s2[i])
            Union[i] = max(s1[i], s2[i])
        else :
            Union[i] = s2[i]

    for key in Intersection :
        a1 += Intersection[key]
    for key in Union :
        a2 += Union[key]

    if a1 == 0 and a2 == 0 :
        return 65536
    else :
        return int((a1 / a2) * 65536)


print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2','AAAA12'))
print(solution('E=M*C^2','e=m*c^2'))
