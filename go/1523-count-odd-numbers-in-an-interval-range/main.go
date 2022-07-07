// Easy
// https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
package main

func countOdds(low int, high int) int {
	ans := (high - low + 1) / 2
	if low%2 == 1 && high%2 == 1 {
		ans++
	}
	return ans
}
