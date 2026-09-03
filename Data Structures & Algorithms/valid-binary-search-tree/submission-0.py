# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = [(root, -float("infinity"), float("infinity"))]
        while q:
            node, lower, upper = q.pop()
            if node.val <= lower or node.val >= upper:
                return False
            if node.left:
                q.append((node.left, lower, min(upper, node.val)))
            if node.right:
                q.append((node.right, max(lower, node.val), upper))
        return True