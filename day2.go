package main

import (
	"fmt"
	"strconv"
	"strings"
)

type instruction struct {
	direction string
	amount    int
}

func DayTwo() {
	lines := GetFileStrings("input/day2.txt")
	values := make([]instruction, len(lines))
	for i, raw := range lines {
		parts := strings.Split(raw, " ")
		values[i].direction = parts[0]
		values[i].amount, _ = strconv.Atoi(strings.TrimSpace(parts[1]))
	}
	fmt.Println("Part One: ", d2partOne(values))
	fmt.Println("Part Two: ", d2partTwo(values))
}

func d2partOne(values []instruction) int {
	x, y := 0, 0
	for _, line := range values {
		if line.direction == "forward" {
			x += line.amount
		}
		if line.direction == "up" {
			y -= line.amount
		}
		if line.direction == "down" {
			y += line.amount
		}
	}
	return x * y
}

func d2partTwo(values []instruction) int {
	x, y, aim := 0, 0, 0
	for _, line := range values {
		if line.direction == "forward" {
			x += line.amount
			y += line.amount * aim
		}
		if line.direction == "up" {
			aim -= line.amount
		}
		if line.direction == "down" {
			aim += line.amount
		}
	}
	return x * y
}
