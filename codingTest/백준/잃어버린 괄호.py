https://www.acmicpc.net/problem/1541
잃어버린 괄호.py

eval() 함수를 써서 계산하면 0으로 시작하는 숫자에서 에러가 뜰 수 있다.
또한 위험한 함수여서 가능하면 사용하지 않는것이 좋다.
+와 -만 사용해서 푸는 문제 라서 쉽게 풀 수 있었다.
+를 먼저해주고 -를 나중에 해주기만 하면 끝

tmp = 0
s = input().split('-')
for i in range(1, len(s)):
    tmp +=  sum(list(map(int,s[i].split('+'))))
print(sum(list(map(int,s[0].split('+'))))- tmp)