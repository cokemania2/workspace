// words.go
// https://www.acmicpc.net/problem/4072

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func printStar(n int) {
	for i := 1; i <= n; i++ {
		str := ""
		for j := 0; j < i; j++ {
			str += "*"
		}
		fmt.Println(str)
	}
}

func main() {
	input := bufio.NewScanner(os.Stdin)

	for true {
		input.Scan()
		word := input.Text()
		wordInt, _ := strconv.Atoi(word)
		if wordInt == 0 {
			break
		} else {
			printStar(wordInt)
		}
	}
}
