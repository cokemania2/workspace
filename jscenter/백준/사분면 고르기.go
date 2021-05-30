// https://www.acmicpc.net/problem/14681
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// use bufio for fast scan
	reader := bufio.NewReader(os.Stdin)

	var x, y int
	fmt.Fscanln(reader, &x)
	fmt.Fscanln(reader, &y)
	if x < 0 {
		if y < 0 {
			fmt.Println(3)
		} else {
			fmt.Println(2)
		}
	} else {
		if y < 0 {
			fmt.Println(4)
		} else {
			fmt.Println(1)
		}
	}
}
