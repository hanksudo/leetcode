from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        prod = 1
        ans = 0
        left = 0
        for right, val in enumerate(nums):
            print(left, right)
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))  # 8
