package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string

	fmt.Scanf("%s", &s)
	slice := strings.Split(s, "-")
	for _, v := range slice {
		fmt.Print(string(v[0]))
	}
}
