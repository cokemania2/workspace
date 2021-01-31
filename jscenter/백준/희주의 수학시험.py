A, B = map(int,input().split(' '))
i = 1
cnt = 0
summ = 0
while True :
    for j in range(0, i) :
        cnt += 1
        if cnt >= A and cnt <= B :
            summ += i
    if cnt > B :
        break
    i += 1
print(summ)
