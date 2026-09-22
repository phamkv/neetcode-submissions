# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        groups = defaultdict(list)
        def dfs(node):
            if not node:
                return 0
            height = max(dfs(node.left), dfs(node.right))
            groups[height].append(node.val)
            return height + 1
        rootNextHeight = dfs(root)
        result = []
        for i in range(rootNextHeight):
            result.append(groups[i])
        return result