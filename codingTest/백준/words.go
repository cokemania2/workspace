// words.go
// https://www.acmicpc.net/problem/4072

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
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
		str := ""
		input.Scan()
		word := input.Text()
		if word == "#" {
			break
		} else {

			slice := strings.Split(word, " ")
			for _, v := range slice {
				str += Reverse(v) + " "
			}
		}
		fmt.Println(str)
	}
}
