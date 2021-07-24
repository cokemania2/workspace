// 부녀회장이 될테야.go
// https://www.acmicpc.net/problem/2775

package main

import (
	"fmt"
)

func main() {
	var T, k, n int
	dp := make([][]int, 15)
	for i := 0; i <= 14; i++ {
		dp[i] = make([]int, 15)
	}
	for i := 0; i < 15; i++ {
		dp[0][i] = i + 1
	}
	for i := 1; i <= 14; i++ {
		for j := 0; j < 15; j++ {
			if j == 0 {
				dp[i][j] = dp[i-1][j]
			} else {
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
			}
		}
	}

	fmt.Scanf("%d", &T)
	for i := 0; i < T; i++ {
		fmt.Scanf("%d", &k)
		fmt.Scanf("%d", &n)
		fmt.Println(dp[k][n-1])
	}

}
