// 손익분기점.go
// https://www.acmicpc.net/problem/1712

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Scan()
	str := input.Text()
	answer := 1

	for i, _ := range str {
		if i >= len(str)-i-1 {
			break
		}
		if str[i] != str[len(str)-i-1] {
			answer = 0
			break
		}
	}
	fmt.Println(answer)
}
