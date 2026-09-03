# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = [root]
        mp = {None: 0}
        while q:
            node = q[-1]
            if node.left and node.left not in mp:
                q.append(node.left)
                continue
            if node.right and node.right not in mp:
                q.append(node.right)
                continue
            node = q.pop()
            l = mp[node.left]
            r = mp[node.right]
            if abs(l-r) > 1:
                return False
            mp[node] = max(l, r) + 1
        return True
            
