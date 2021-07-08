// 손익분기점.go
// https://www.acmicpc.net/problem/1712

package main

import (
	"fmt"
)

func main() {
	var A, B, C int

	fmt.Scanf("%d %d %d", &A, &B, &C)
	if C-B <= 0 {
		fmt.Println(-1)
	} else {
		BEP := int(A / (C - B))
		fmt.Println(BEP + 1)
	}
}
