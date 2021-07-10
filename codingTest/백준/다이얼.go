package main

import (
	"fmt"
)

func main() {
	var s string
	sum := 0
	dial := []int{2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9}

	fmt.Scanf("%s", &s)
	for _, v := range s {
		sum += dial[v-'A'] + 1
	}
	fmt.Println(sum)
}
