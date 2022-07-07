package main

import "fmt"

func binaryGap(n int) int {
	ans := 0
	last := -1
	pos := 0
	for {
		if n == 0 {
			return ans
		}
		i := n % 2
		n /= 2
		if i == 1 {
			if last < 0 {
				last = pos
			} else if pos-last > ans {
				ans = pos - last
			}
			last = pos
		}
		pos += 1
	}
}

func main() {
	fmt.Println(binaryGap(15) == 1)
	fmt.Println(binaryGap(22) == 2)
}
