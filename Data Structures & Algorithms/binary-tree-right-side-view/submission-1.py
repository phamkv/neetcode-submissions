# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        seenHeight = set()
        result = []
        q = [(root, 0)]
        while q:
            for _ in range(len(q)):
                node, h = q.pop()
                if node.left:
                    q.append((node.left, h+1))
                if node.right:
                    q.append((node.right, h+1))
                if h in seenHeight:
                    continue
                result.append(node.val)
                seenHeight.add(h)
        return result