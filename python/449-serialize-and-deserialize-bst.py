# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from math import inf
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def pre_order(root):
            if root is None:
                return ""

            vals.append(str(root.val))
            pre_order(root.left)
            pre_order(root.right)
        pre_order(root)
        return " ".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        queue = data.split(" ")

        def helper(q, min_value, max_value):
            if not q:
                return

            val = int(q[0])
            if val < min_value or val > max_value:
                return
            q.pop(0)
            root = TreeNode(val)
            root.left = helper(q, min_value, val)
            root.right = helper(q, val, max_value)
            return root
        return helper(queue, -inf, inf)

def pre_order(root):
    if root is None:
        return None
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)

if __name__ == "__main__":

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    codec = Codec()
    node = codec.deserialize(codec.serialize(root))

    pre_order(node) # 2 1 3
