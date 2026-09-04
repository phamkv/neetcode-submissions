# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return (0, True)
            lh, lc = height(node.left)
            rh, rc = height(node.right)
            if lc and rc:
                if abs(lh - rh) > 1:
                    return (0, False)
                return (max(lh, rh) + 1, True)
            return (0, False)
        h, c = height(root)
        return c