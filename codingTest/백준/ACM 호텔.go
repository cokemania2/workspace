// ACM 호텔.go
// https://www.acmicpc.net/problem/10250

package main

import (
	"fmt"
	"strconv"
)

func main() {
	var T int
	fmt.Scanf("%d", &T)
	for i := 0; i < T; i++ {
		var H, W, N int
		answer := ""

		fmt.Scanf("%d %d %d", &H, &W, &N)
		if N%H == 0 {
			answer = strconv.Itoa(H)
			if (N / H) < 10 {
				answer += "0" + strconv.Itoa(N/H)
			} else {
				answer += strconv.Itoa(N / H)
			}
		} else {
			answer += strconv.Itoa(N % H)
			if (N/H + 1) < 10 {
				answer += "0" + strconv.Itoa(N/H+1)
			} else {
				answer += strconv.Itoa(N/H + 1)
			}
		}
		fmt.Println(answer)
	}
}
