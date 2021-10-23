// https://programmers.co.kr/learn/courses/30/lessons/87389?language=go
// 나머지가 1이 되는 수 찾기.go

func solution(n int) int {
	for i := 2; i < n; i++ {
		if (n-1)%i == 0 {
			return i
		}
	}
	return n - 1
}