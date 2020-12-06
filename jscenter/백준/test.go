package main

import (
	"fmt"
	"sort"
)

func main() {
	sum := 0
	var arr [8]int
	for i := 0; i < 8; i++ {
		fmt.Scan(&arr[i])
	}
	sort.Ints(arr)
	fmt.Print(sum / 5)
}
