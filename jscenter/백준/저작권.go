// https://www.acmicpc.net/problem/2914
// 저작권.go

package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)
	fmt.Println(a*(b-1) + 1)
}
