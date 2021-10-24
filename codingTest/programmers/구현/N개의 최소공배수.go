// N개의 최소공배수.go
// https://programmers.co.kr/learn/courses/30/lessons/12953?language=go

func gcd(x int, y int) int {
	if x%y == 0 {
		return y
	} else {
		return gcd(y, x%y)
	}
}

func lcm(x int, y int) int {
	return (x * y) / gcd(x, y)
}

func solution(arr []int) int {
	answer := 1
	for i := 1; i < len(arr); i++ {
		answer = lcm(answer, lcm(arr[i-1], arr[i]))
	}

	return answer
}