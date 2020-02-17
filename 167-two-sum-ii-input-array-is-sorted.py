class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1
        while left_index < right_index:
            number_sum = numbers[left_index] + numbers[right_index]
            if number_sum == target:
                return [left_index + 1, right_index + 1]
            elif number_sum < target:
                left_index += 1
            elif number_sum > target:
                right_index -= 1
