package main

import (
	"os"
)

func main() {
	choice := os.Args[1:]

	switch choice[0] {
	case "1":
		DayOne()
	case "2":
		DayTwo()
	case "3":
		DayThree()
	}
}
