# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        q = [(root, root.val-1)]
        while q:
            node, biggest = q.pop()
            if node.val >= biggest:
                result += 1
            biggest = max(biggest, node.val)
            if node.left:
                q.append((node.left, biggest))
            if node.right:
                q.append((node.right, biggest))
        return result