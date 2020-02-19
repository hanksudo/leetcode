# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Reverse Post Order solution
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         if root is None:
#             return

#         left_tree = []

#         def pre_order(root):
#             if root is None:
#                 return
#             left_tree.append(root)
#             pre_order(root.left)
#             pre_order(root.right)

#         if root.left:
#             pre_order(root.left)

#         root.left = None
#         while left_tree:
#             node = left_tree.pop()
#             node.left = None
#             node.right = root.right
#             root.right = node

# Pre order solution
class Solution:
    prev = None
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        self.pre_order(root)

    def pre_order(self, root):
        if root is None:
            return

        left = root.left
        right = root.right

        if self.prev is None:
            root.left = None
            self.prev = root
        else:
            root.left = None
            self.prev.right = root
            self.prev = root

        self.pre_order(left)
        self.pre_order(right)
