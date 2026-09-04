# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        currLevel = 0
        queue = deque([(root, 0)])
        result = []
        levelA = []
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            if currLevel < level:
                result.append(levelA)
                levelA = []
                currLevel = level
            levelA.append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        if levelA:
            result.append(levelA)
        return result