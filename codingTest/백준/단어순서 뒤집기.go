// 단어순서 뒤집기.go
// https://www.acmicpc.net/problem/12605

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var N int
	input := bufio.NewScanner(os.Stdin)

	fmt.Scanf("%d", &N)
	for i := 0; i < N; i++ {
		input.Scan()
		fmt.Print("Case #" + strconv.Itoa(i+1) + ": ")
		slice := strings.Split(input.Text(), " ")
		for j := len(slice) - 1; j >= 0; j-- {
			fmt.Print(slice[j] + " ")
		}
		fmt.Println()
	}
}
