# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        seen = set()
        result = []
        while q:
            node = q[-1]
            if node.right and node.right not in seen:
                seen.add(node.right)
                node = q.pop()
                q.append(node.right)
                q.append(node)
                continue
            if node.left and node.left not in seen:
                seen.add(node.left)
                q.append(node.left)
                continue
            node = q.pop()
            result.append(node.val)
        return result[k-1]
            
            
