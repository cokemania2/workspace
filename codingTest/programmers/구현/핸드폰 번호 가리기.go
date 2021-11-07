// https://programmers.co.kr/learn/courses/30/lessons/12948?language=go
// 핸드폰 번호 가리기.go

// func Repeat(s string, count int) string: 문자열을 특정 횟수만큼 반복
// for문을 빼고 Repeat으로 넣을 수 있다.

func solution(phone_number string) string {
	answer := ""
	secret_n := len(phone_number) - 4
	for i := 0; i < secret_n; i++ {
		answer += "*"
	}
	answer += phone_number[secret_n:]
	return answer
}