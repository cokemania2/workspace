// https://www.acmicpc.net/problem/3052

package main

import (
	"fmt"
)

func main() {
	idMap := make(map[int]bool, 10)

	for i := 0; i < 10; i++ {
		var v int
		fmt.Scanln(&v)
		_, exist := idMap[v%42]
		if !exist {
			idMap[v%42] = true
		}
	}
	fmt.Println(len(idMap))
}
