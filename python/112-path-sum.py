# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        def helper(root, sum):
            if root is None:
                return False

            if root.left is None and root.right is None:
                return root.val == sum

            return helper(root.left, sum - root.val) or helper(root.right, sum - root.val)

        return helper(root, sum)
