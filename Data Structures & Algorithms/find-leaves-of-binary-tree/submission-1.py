# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(node):
            if not node:
                return 0
            height = max(dfs(node.left), dfs(node.right))
            if len(result) <= height:
                result.append([])
            result[height].append(node.val)
            return height + 1
        dfs(root)
        return result