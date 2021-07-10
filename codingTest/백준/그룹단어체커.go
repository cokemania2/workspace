// 그룹단어체커.go
// https://www.acmicpc.net/problem/1316

package main

import (
	"fmt"
)

func main() {
	var N int

	answer := 0

	fmt.Scanln(&N)
	for i := 0; i < N; i++ {
		var str string
		var before rune
		slice := make([]bool, 26)
		flag := true

		fmt.Scanln(&str)
		slice[str[0]-'a'] = true
		before = rune(str[0])
		for _, s := range str {
			if slice[s-'a'] {
				if before == s {
					continue
				} else {
					flag = false
					break
				}
			} else {
				slice[s-'a'] = true
				before = s
			}
		}
		if flag {
			answer += 1
		}
	}
	fmt.Println(answer)
}
