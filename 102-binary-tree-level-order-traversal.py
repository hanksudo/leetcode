# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        vals = []
        level = 0
        queue = [(root, level)]
        while queue:
            # dequeue
            node, level = queue.pop(0)
            if len(vals) < level + 1:
                vals.append([node.val])
            else:
                vals[level].append(node.val)

            # enqueue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return vals
