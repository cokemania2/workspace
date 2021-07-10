# 욱제는 결정장애야!!
# https://www.acmicpc.net/problem/14646

# 매번 돌림판을 돌리며 선택지가 가장 많을 경우를 출력해준다.

dic = {}
mx = 0
N = int(input())
menu = list(map(int,input().split(' ')))
for i in menu :
    if i in dic :
        del dic[i]
    else :
        dic[i] = True
    if len(dic) > mx :
        mx = len(dic)
print(mx)
