# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []

        def find_paths(root, sum, path):
            if root is None:
                return

            path.append(root.val)
            if root.left is None and root.right is None and root.val == sum:
                paths.append(path)
                return

            find_paths(root.left, sum - root.val, path[:])
            find_paths(root.right, sum - root.val, path[:])

        find_paths(root, sum, [])
        return paths
