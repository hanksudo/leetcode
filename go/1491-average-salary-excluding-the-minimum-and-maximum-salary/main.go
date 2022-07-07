// Easy
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

package main

import (
	"fmt"
	"math"
)

func average(salary []int) float64 {
	min := math.MaxInt
	max := math.MinInt
	var sum int

	for _, n := range salary {
		if n > max {
			max = n
		}
		if n < min {
			min = n
		}
		fmt.Println(min, max)

		sum += n
	}
	return float64(sum-min-max) / float64(len(salary)-2)
}
