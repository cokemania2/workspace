// https://www.acmicpc.net/problem/2577
// 숫자의 개수
// 자료형 rune이 있다. rune은 유니코드를 쉽게 제어하기 위한 타입으로서
// Go 언어의 rune타입은 int32를 재정의 해서 사용하고 있다.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	// use bufio for fast scan
	reader := bufio.NewReader(os.Stdin)

	var A, B, C int
	dict := make(map[rune]int)

	fmt.Fscan(reader, &A, &B, &C)
	sum := strconv.Itoa(A * B * C)

	for _, num := range sum {
		if val, ok := dict[num]; ok {
			dict[num] = val + 1
		} else {
			dict[num] = 1
		}
	}
	for _, num := range "0123456789" {
		if val, ok := dict[num]; ok {
			fmt.Println(val)
		} else {
			fmt.Println(0)
		}
	}
}
