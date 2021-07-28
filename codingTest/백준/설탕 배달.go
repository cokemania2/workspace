// 설탕 배달.go
// https://www.acmicpc.net/problem/2839

package main

import (
	"fmt"
)

func solution(N int) int {
	count := 0
	for N >= 0 {
		if N%5 == 0 {
			return N/5 + count
		} else {
			N -= 3
			count += 1
		}
	}
	return -1
}

func main() {
	var N int

	fmt.Scanf("%d", &N)
	fmt.Println(solution(N))
}
