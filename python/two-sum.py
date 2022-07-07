# https://leetcode.com/problems/two-sum

# O(n^2)
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# O(n)
def twoSum(nums, target):
    data = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in data:
            return [data[complement], i]
        data[nums[i]] = i

if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
