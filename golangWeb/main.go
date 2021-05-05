package main

import (
	"net/http"

	"github.com/cokemania2/golangWeb/myapp"
)

func main() {
	// 웹 서버 실행
	http.ListenAndServe(":3000", myapp.NewHttpHandler())
}
