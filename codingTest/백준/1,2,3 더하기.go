// 1, 2, 3 더하기.go
// https://www.acmicpc.net/problem/9095

package main

import (
	"fmt"
)

func main() {
	var T, N int
	dp := make([]int, 12)
	dp[1] = 1
	dp[2] = 2
	dp[3] = 4
	for i := 4; i <= 10; i++ {
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	}
	fmt.Scanf("%d", &T)
	for i := 0; i < T; i++ {
		fmt.Scanf("%d", &N)
		fmt.Println(dp[N])
	}
}
