# https://programmers.co.kr/learn/courses/30/lessons/76501?language=go
# 음양 더하기.py

func solution(absolutes []int, signs []bool) int {
    answer := 0
    sign := 1
    for i, v := range(absolutes) {
        if signs[i] {
            sign = 1
        } else {
            sign = -1
        }
        answer += v * sign
    }
    return answer
}