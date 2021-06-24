// https://www.acmicpc.net/problem/2562

package main

import (
	"fmt"
)

func main() {
	// use bufio for fast scan
	maxValue := 0
	maxIndex := 0

	for i := 0; i < 9; i++ {
		var v int
		fmt.Scanln(&v)
		if v > maxValue {
			maxValue = v
			maxIndex = i + 1
		}
	}
	fmt.Println(maxValue)
	fmt.Println(maxIndex)
}
