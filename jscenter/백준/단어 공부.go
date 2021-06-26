// https://www.acmicpc.net/problem/1157
// 단어 공부

package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	alpha := make(map[string]int)
	max := 0
	answer := ""

	fmt.Scanf("%s", &s)
	s = strings.ToUpper(s)
	for _, v := range s {
		if _, ok := alpha[string(v)]; ok {
			alpha[string(v)] += 1
		} else {
			alpha[string(v)] = 0
		}
	}
	for key, value := range alpha {
		if value > max {
			max = value
			answer = key
		} else if value == max {
			answer += key
		}
	}
	if len(answer) == 1 {
		fmt.Println(answer)
	} else {
		fmt.Println("?")
	}
}
