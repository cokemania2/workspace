// https://www.acmicpc.net/problem/11945
// 뜨거운 붕어빵

package main

import (
	"fmt"
)

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	var N, M int
	fmt.Scanf("%d %d", &N, &M)

	for i := 0; i < N; i++ {
		var s string
		fmt.Scanln(&s)
		fmt.Println(Reverse(s))
	}
}
