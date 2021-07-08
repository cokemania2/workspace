// 주사위 게임.go
// https://www.acmicpc.net/problem/10103
package main

import (
	"fmt"
)

func main() {
	var N int
	var a, b int
	A := 100
	B := 100

	fmt.Scanln(&N)
	for i := 0; i < N; i++ {
		fmt.Scanf("%d %d\n", &a, &b)
		if a > b {
			B -= a
		} else if a < b {
			A -= b
		}
	}
	fmt.Println(A)
	fmt.Println(B)
}
