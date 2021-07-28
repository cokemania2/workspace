// 영수증.go
// https://www.acmicpc.net/problem/5565

package main

import (
	"fmt"
)

func main() {
	var v, total int
	fmt.Scanf("%d", &total)
	for i := 0; i < 9; i++ {
		fmt.Scanf("%d", &v)
		total -= v
	}
	fmt.Println(total)
}
