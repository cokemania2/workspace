// https://www.acmicpc.net/problem/10818

package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	mySlice := make([]int, 0)

	fmt.Scanln(&N)
	for i := 0; i < N; i++ {
		var v int

		fmt.Scan(&v)
		mySlice = append(mySlice, v)
	}
	sort.Ints(mySlice)
	fmt.Println(mySlice[0], mySlice[len(mySlice)-1])
}
