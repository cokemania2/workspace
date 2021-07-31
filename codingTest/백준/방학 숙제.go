// 방학 숙제.go
// https://www.acmicpc.net/problem/5532

package main

import (
	"fmt"
)

func main() {
	var L, A, B, C, D int
	answer := 0
	fmt.Scanf("%d", &L)
	fmt.Scanf("%d", &A)
	fmt.Scanf("%d", &B)
	fmt.Scanf("%d", &C)
	fmt.Scanf("%d", &D)
	if A/C > B/D {
		answer = L - A/C
		if A%C != 0 {
			answer -= 1
		}
	} else {
		answer = L - B/D
		if B%D != 0 {
			answer -= 1
		}
	}
	fmt.Println(answer)
}
