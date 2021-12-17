package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

func GetFileStrings(path string) []string {
	inputMem, _ := ioutil.ReadFile(path)
	lines := strings.Split(string(inputMem), "\n")
	return lines
}

func GetFileInts(path string) []int {
	file := GetFileStrings(path)
	values := make([]int, len(file))
	for i, raw := range file {
		values[i], _ = strconv.Atoi(strings.TrimSpace(raw))
	}
	return values
}
