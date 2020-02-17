# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from math import inf
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateBST(root, -inf, inf)

    def validateBST(self, root, min_value, max_value):
        if root is None:
            return True
        return (
            root.val < max_value and
            root.val > min_value and
            self.validateBST(root.left, min_value, root.val) and
            self.validateBST(root.right, root.val, max_value)
        )
