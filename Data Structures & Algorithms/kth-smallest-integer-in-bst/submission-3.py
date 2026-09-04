# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #intraversal l n r dfs
        i = 0
        result = 0
        def dfs(node):
            nonlocal i, result
            if not node:
                return
            dfs(node.left)
            if i >= k:
                return
            i += 1
            if i == k:
                result = node.val
                return
            dfs(node.right)
        dfs(root)
        return result
            

