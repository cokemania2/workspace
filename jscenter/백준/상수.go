// https://www.acmicpc.net/problem/2908
// 상수

package main

import (
	"fmt"
	"math"
	"strconv"
)

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	var a, b string

	fmt.Scanf("%s %s", &a, &b)
	a = Reverse(a)
	b = Reverse(b)
	A, _ := strconv.Atoi(a)
	B, _ := strconv.Atoi(b)
	fmt.Println(math.Max(float64(A), float64(B)))
}
