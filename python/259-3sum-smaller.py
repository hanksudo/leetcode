class Solution:
    def threeSumSmaller(self, nums, target):
        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            # if nums[i] >= target:
            #     break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] >= target:
                    r -= 1
                else:
                    res += (r - l)
                    l += 1

        return res

if __name__ == "__main__":
    print(Solution().threeSumSmaller([-2, 0, 1, 3], 2))  # 2
    print(Solution().threeSumSmaller([5, 1, 3, 4, 7], 12))  # 4
