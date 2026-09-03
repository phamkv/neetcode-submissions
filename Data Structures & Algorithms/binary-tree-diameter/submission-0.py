# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        mp = {None: (0,0)}
        q = [root]
        while q:
            node = q[-1]
            if node.left and node.left not in mp:
                q.append(node.left)
                continue
            if node.right and node.right not in mp:
                q.append(node.right)
                continue
            node = q.pop()
            lH, lD = mp[node.left]
            rH, rD = mp[node.right]
            h = max(lH, rH) + 1
            d = max(lH + rH, lD, rD)
            mp[node] = (h, d)
        return mp[root][1]