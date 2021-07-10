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

	var str string
	var sum int
	for i := 0; i < 5; i++ {
		fmt.Fscanln(reader, &str)
		inteager, _ := strconv.Atoi(str)
		if inteager <= 40 {
			inteager = 40
		}
		sum += inteager
	}
	fmt.Println(sum / 5)
}
