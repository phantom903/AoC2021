package main

import (
	"fmt"
)

func DayOne() int {
	values := GetFileInts("input/day1.txt")
	fmt.Println("Part One: ", d1partOne(values))
	fmt.Println("Part Two: ", d1partTwo(values))
	return 1
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
