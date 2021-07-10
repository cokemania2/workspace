package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// use bufio for fast scan
	reader := bufio.NewReader(os.Stdin)

	var A, B int

	fmt.Fscan(reader, &A, &B)
	if A > B {
		fmt.Println(">")
	} else if A < B {
		fmt.Println("<")
	} else {
		fmt.Println("==")
	}
}
