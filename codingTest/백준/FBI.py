flag = False
for i in range (5) :
    if input().find('FBI') != -1 :
        flag = True
        print(i + 1,end = ' ')
if flag == False :
    print("HE GOT AWAY!")