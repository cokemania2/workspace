package main

import "fmt"

func main() {
	var T int
	fmt.Scan(&T)
	for i := 0; i < T; i++ {
		var str string
		fmt.Scan(&str)
		fmt.Println(str[0], str[:1])
	}
}
