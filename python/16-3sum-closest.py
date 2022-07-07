from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = sum(nums[:3])

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return res
        return res

if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))  # 2
    print(Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))  # 82
