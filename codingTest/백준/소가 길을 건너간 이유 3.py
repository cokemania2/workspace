# https://www.acmicpc.net/problem/14469
# 소가 길을 건너간 이유 3.py

# 소의 도착시간에 맞추어 정렬을 해준다음
# 소의 도착시간 < 마지막 통과 시간 이면
#     마지막 통과시간 이후 소가 바로 들어가기 때문에
#     소비시간에 소의 검문시간을 더해준다
# 나머지는
#     소의 도착시간에서 마지막 통과시간을 빼준 후 검문시간을 더한값을 더해주면 된다.  

i_list = []
N = int(input())
for i in range(N):
    i_list.append(list(map(int, input().split())))
i_list = sorted(i_list, key=lambda x : x[0])
spent_time = sum(i_list[0])
last_time = sum(i_list[0])
for i in range(1, len(i_list)):
    if i_list[i][0] <= last_time:
        spent_time +=  i_list[i][1]
        last_time += i_list[i][1]
    else:
        spent_time += i_list[i][0] - spent_time + i_list[i][1]
        last_time = sum(i_list[i])
print(spent_time)