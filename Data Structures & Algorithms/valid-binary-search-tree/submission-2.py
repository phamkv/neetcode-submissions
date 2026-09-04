# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBst(node, smallestV, biggestV):
            if not node:
                return True
            if node.val <= smallestV:
                return False
            if node.val >= biggestV:
                return False
            return isBst(node.left, smallestV, node.val) and isBst(node.right, node.val, biggestV)
        return isBst(root, -float("infinity"), float("infinity"))