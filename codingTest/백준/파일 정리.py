from audioop import reverse


n = int(input())
dic = {}
for i in range(n):
    file_ext = input().split('.')[1]
    if file_ext in dic:
        dic[file_ext] += 1
    else:
        dic[file_ext] = 1

for key in list(sorted(list(dic.keys()))):
    print(key, dic[key])