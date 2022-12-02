package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	beats = map[string]string{
		"A": "C",
		"B": "A",
		"C": "B",
	}
	translation = map[string]string{
		"X": "A",
		"Y": "B",
		"Z": "C",
	}
	points = map[string]int{
		"A": 1,
		"B": 2,
		"C": 3,
		"X": 1,
		"Y": 2,
		"Z": 3,
	}
)

func main() {
	score := 0
	for scanner := bufio.NewScanner(os.Stdin); scanner.Scan(); {
		line := strings.Split(scanner.Text(), " ")
		enemy, me := line[0], translation[line[1]]
		if beats[enemy] == me {
			score += points[me]
		} else if beats[me] == enemy {
			score += points[me] + 6
		} else {
			score += points[me] + 3
		}
	}
	fmt.Println(score)
}
