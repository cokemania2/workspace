// 고무오리 디버깅.go
// https://www.acmicpc.net/problem/20001

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	stack := 0

	for true {
		input.Scan()
		str := input.Text()
		if str == "고무오리" {
			if stack == 0 {
				stack += 2
			} else {
				stack -= 1
			}
		} else if str == "문제" {
			stack += 1
		} else if str == "고무오리 디버깅 끝" {
			if stack == 0 {
				fmt.Println("고무오리야 사랑해")
			} else {
				fmt.Println("힝구")
			}
			break
		}
	}
}
