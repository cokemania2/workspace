// K번쨰수.go
// https://programmers.co.kr/learn/courses/30/lessons/42748?language=go

package main

import (
	"fmt"
	"sort"
)

func solution(array []int, commands [][]int) []int {
	answer := make([]int, 0)
	for _, command := range commands {
		slice := make([]int, command[1]-command[0]+1)
		copy(slice, array[command[0]-1:command[1]])
		sort.Ints(slice)
		answer = append(answer, slice[command[2]-1])
	}
	return answer
}

func main() {
	array := []int{1, 5, 2, 6, 3, 7, 4}
	commands := [][]int{{2, 5, 3}, {4, 4, 1}, {1, 7, 3}}
	fmt.Println(solution(array, commands))
}
