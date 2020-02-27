from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    assert Solution().findPeakElement([1, 2, 3, 1]) == 2
    assert Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
