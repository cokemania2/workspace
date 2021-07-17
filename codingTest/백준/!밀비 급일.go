// !밀비 급일.go
// https://www.acmicpc.net/problem/11365

package main

import (
	"bufio"
	"fmt"
	"os"
)

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	for true {
		input.Scan()
		str := input.Text()
		if str == "END" {
			break
		} else {
			fmt.Println(Reverse(str))
		}
	}
}
