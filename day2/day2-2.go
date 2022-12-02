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
	loses = map[string]string{
		"C": "A",
		"A": "B",
		"B": "C",
	}
	points = map[string]int{
		"A": 1,
		"B": 2,
		"C": 3,
	}
)

func main() {
	score := 0
	for scanner := bufio.NewScanner(os.Stdin); scanner.Scan(); {
		line := strings.Split(scanner.Text(), " ")
		switch enemy, outcome := line[0], line[1]; outcome {
		case "X":
			score += points[beats[enemy]]
		case "Z":
			score += points[loses[enemy]] + 6
		default:
			score += points[enemy] + 3
		}
	}
	fmt.Println(score)
}
