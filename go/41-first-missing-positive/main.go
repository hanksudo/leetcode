package main

import "fmt"

func firstMissingPositive(nums []int) int {
	for i := 0; i < len(nums); i++ {
		if nums[i] < 0 {
			nums[i] = 0
		}
	}
	for i := 0; i < len(nums); i++ {
		val := nums[i]
		if val < 0 {
			val *= -1
		}
		if val >= 1 && val <= len(nums) {
			if nums[val-1] > 0 {
				nums[val-1] *= -1
			} else if nums[val-1] == 0 {
				nums[val-1] = (len(nums) + 1) * -1
			}

		}
	}
	for i := 0; i < len(nums); i++ {
		if nums[i] >= 0 {
			return i + 1
		}
	}
	return len(nums) + 1
}

func main() {
	fmt.Println(firstMissingPositive([]int{1, 2, 0}) == 3)
	fmt.Println(firstMissingPositive([]int{3, 4, -1, 1}) == 2)
	fmt.Println(firstMissingPositive([]int{7, 8, 9, 11, 12}) == 1)
}
