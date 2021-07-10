##https://www.acmicpc.net/problem/6996

T = int(input())
for i in range(T) :
    A, B = input().split(' ')
    a = list(A)
    b = list(B)
    if len(A) != len(B) :
        print(A,'&',B,'are NOT anagrams.')
        continue
    for i in a :
        if str(b).find(i) != -1:
            b.pop(b.index(i))
        else :
            print(A,'&',B,'are NOT anagrams.')
            break
    if len(b) == 0 :
        print(A,'&',B,'are anagrams.')
