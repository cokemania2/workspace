// https://www.acmicpc.net/problem/9086
// 문자열의 맨앞 문자와 맨 뒤 문자를 더하는 문제
// bufio를 사용하면 입/출력의 속도가 빠르다.

package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var length int

	// use bufio for fast scan
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	fmt.Fscanln(reader, &length)

	var str string

	for i := 0; i < length; i++ {
		fmt.Fscanln(reader, &str)
		fmt.Fprintln(string(str[0]) + string(str[len(str)-1]))
	}

}
