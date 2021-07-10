// Darius님 한타 안 함?
// https://www.acmicpc.net/problem/20499

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var s string

	fmt.Scanf("%s", &s)
	slice := strings.Split(s, "/")
	kill, _ := strconv.Atoi(slice[0])
	death, _ := strconv.Atoi(slice[1])
	assist, _ := strconv.Atoi(slice[2])
	if death == 0 || kill+assist < death {
		fmt.Println("hasu")
	} else {
		fmt.Println("gosu")
	}
}
