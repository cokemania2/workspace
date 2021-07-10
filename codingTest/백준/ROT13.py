##https://www.acmicpc.net/problem/11655
##ROT13

s = list(input())
for i in s :
    if i.isupper() and ord(i) + 13 > ord('Z') :
        print(chr(ord('A') + (ord(i) + 12 - ord('Z'))), end ='')
    elif i.islower() and ord(i) + 13 > ord('z') :
        print(chr(ord('a') + (ord(i) + 12 - ord('z'))), end ='')
    elif i.isalpha()  :
        print(chr(ord(i) +13), end ='')
    else :
        print(i, end='')