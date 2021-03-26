package main

func twoSum(nums []int, target int) []int {
	var ans []int
	m := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		_, exists := m[complement]
		if exists {
			ans = []int{m[complement], i}
		}
		m[num] = i
	}
	return ans
}
