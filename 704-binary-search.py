class Solution:
    # recursive
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, low, high, target):
            if low > high:
                return -1
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return helper(nums, mid + 1, high, target)
            else:
                return helper(nums, low, mid - 1, target)

        return helper(nums, 0, len(nums) - 1, target)

    # iterative
    # def search(self, nums: List[int], target: int) -> int:
    #     low = 0
    #     high = len(nums) - 1

    #     while low <= high:
    #         mid = (high + low) // 2
    #         if target == nums[mid]:
    #             return mid
    #         elif target > nums[mid]:
    #             low = mid + 1
    #         else:
    #             high = mid - 1

    #     return -1
