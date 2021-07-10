// https://www.acmicpc.net/problem/11179
// 2진수 뒤집기

package main

import (
	"fmt"
	"math"
)

func main() {
	var i int
	answer := 0.0
	fmt.Scanf("%d", &i)
	s := fmt.Sprintf("%b", i)
	for i, v := range s {
		intV := int(v - '0')
		if intV == 1 {
			answer += math.Pow(2, float64(i))
		}
	}
	fmt.Println(int(answer))
}
