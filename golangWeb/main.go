package main

import (
	"fmt"
	"net/http"
)

func main() {
	// 어떤 경로에 들어왔을때 어떤 행동을 할것인지 핸들러
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "Hello world")
	})
	http.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "hello Bar!")
	})
	// 웹 서버 실행
	http.ListenAndServe(":3000", nil)
}
