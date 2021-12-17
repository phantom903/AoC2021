package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	inputMem, _ := ioutil.ReadFile("input/day1.txt")
	lines := strings.Split(string(inputMem), "\n")
	values := make([]int, len(lines))
	for i, raw := range lines {
		values[i], _ = strconv.Atoi(strings.TrimSpace(raw))
	}
	fmt.Println("Part One: ", d1partOne(values))
	fmt.Println("Part Two: ", d1partTwo(values))
}

func d1partOne(values []int) int {
	count := 0
	for i := 0; i < len(values)-1; i++ {
		if values[i] < values[i+1] {
			count += 1
		}
	}
	return count
}

func d1partTwo(inputMem []int) int {
	count := 0
	for i := 0; i < len(inputMem)-3; i++ {
		tot1 := inputMem[i] + inputMem[i+1] + inputMem[i+2]
		tot2 := inputMem[i+1] + inputMem[i+2] + inputMem[i+3]
		if tot2 > tot1 {
			count += 1
		}
	}
	return count
}
