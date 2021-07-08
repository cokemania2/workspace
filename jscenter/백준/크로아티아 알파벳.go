// 크로아티아 알파벳.go
// https://www.acmicpc.net/problem/2941

package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	dummy := []string{"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}

	fmt.Scanf("%s", &s)
	for _, v := range dummy {
		if indexS := strings.Index(s, v); indexS != -1 {
			s = strings.ReplaceAll(s, v, "0")
		}
	}
	fmt.Println(len(s))
}
