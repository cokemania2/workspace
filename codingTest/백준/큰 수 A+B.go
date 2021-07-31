// 큰 수 A+B.go
// https://www.acmicpc.net/problem/10757

package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
)

var reader = bufio.NewReader(os.Stdin)
var scanner = bufio.NewScanner(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func init() {
	scanner.Split(bufio.ScanWords)
}

func nextInt() int {
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	return n
}

func main() {
	defer writer.Flush()
	var n, m big.Int

	fmt.Fscan(reader, &n, &m)

	add := new(big.Int)
	add = add.Add(&n, &m)
	fmt.Println(add)
}
