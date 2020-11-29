package main

import "fmt"

func main() {
	sum := 0
	var n int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)
		sum += a
	}
	fmt.Print(sum / n)
}
