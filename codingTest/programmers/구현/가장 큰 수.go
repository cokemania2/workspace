// https://programmers.co.kr/learn/courses/30/lessons/42746?language=go
// 가장 큰 수.go

import (
	"sort"
	"strconv"
)

func solution(numbers []int) string {
	answer := ""
	sort.Slice(numbers, func(i, j int) bool {
		a, _ := strconv.Atoi(strconv.Itoa(numbers[i]) + strconv.Itoa(numbers[j]))
		b, _ := strconv.Atoi(strconv.Itoa(numbers[j]) + strconv.Itoa(numbers[i]))
		if a > b {
			return true
		} else {
			return false
		}
	})
	for i, number := range numbers {
		if i == 0 && number == 0 {
			return "0"
		}
		answer += strconv.Itoa(number)
	}
	return answer
}