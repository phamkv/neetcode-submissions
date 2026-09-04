# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node):
            if not node:
                return (0, 0)
            lh, ld = diameter(node.left)
            rh, rd = diameter(node.right)
            h = max(lh, rh) + 1
            d = max(lh + rh, ld, rd)
            return (h, d)
        h, d = diameter(root)
        return d