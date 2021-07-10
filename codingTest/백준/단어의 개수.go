// https://www.acmicpc.net/problem/1152

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// use bufio for fast scan
	reader := bufio.NewReader(os.Stdin)

	S, _ := reader.ReadString('\n')
	S = strings.TrimSpace(S)
	slice := strings.Split(S, " ")
	if S == "" {
		fmt.Println(0)
	} else {
		fmt.Println(len(slice))
	}
}
