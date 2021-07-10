# https://www.acmicpc.net/submit/14910/11526155
# 오르막
# 정렬을 해서 이전 리스트와 같으면 오름차순..

N = list(map(int,input().split()))
B = sorted(N)
if (N == B) :
    print('Good')
else :
    print('Bad')
