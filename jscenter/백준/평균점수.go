package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 5; i++ {
		var n int
		fmt.Scan(&n)
		if n < 40 {
			n = 40
		}
		sum += n
	}
	fmt.Print(sum / 5)
}
