// https://www.acmicpc.net/problem/2789

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func isCAMBRIDGE(s rune) bool {
	baseWord := "CAMBRIDGE"
	for _, word := range baseWord {
		if s == word {
			return true
		}
	}
	return false
}

func main() {
	// use bufio for fast scan
	reader := bufio.NewReader(os.Stdin)
	s, _ := reader.ReadString('\n')

	answer := []string{}
	for _, word := range s {
		if !isCAMBRIDGE(word) {
			answer = append(answer, string(word))
		}
	}
	fmt.Println(strings.Join(answer, ""))
}
