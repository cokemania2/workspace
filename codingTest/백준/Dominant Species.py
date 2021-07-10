##https://www.acmicpc.net/problem/10175
##Dominant Species

# 각각 쌘 정도가 있어서 * vlaue 를 해줘야한다.
# dictionary의 value를 max로 뽑는 방법이 있어서 썼고
# 중복제거를 위해서 list로 다시 만들고 앞의 두 값을 비교해서 중복체크를 했다.

n = int(input())
dic = {}
for i in range(n) :
    s = list(input().split(' '))
    dic['Bobcat'] = s[1].count('B') * 2 
    dic['Coyote'] = s[1].count('C') * 1
    dic['Mountain Lion'] = s[1].count('M') * 4
    dic['Wolf'] = s[1].count('W') * 3
    king = max(dic,key = dic.get)
    a = sorted(dic.values(), reverse = True)
    print(s[0] + ': ',end ='')
    if a[0] == a[1] :
        print('There is no dominant species')
    else :
        print('The ' + king + ' is the dominant species')
