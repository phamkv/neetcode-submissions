# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            pq = [p]
            qq = [q]
            while pq or qq:
                pn = pq.pop()
                qn = qq.pop()
                if not pn and qn or pn and not qn:
                    return False
                if not pn and not qn:
                    continue
                if pn.val != qn.val:
                    return False
                pq.append(pn.left)
                pq.append(pn.right)
                qq.append(qn.left)
                qq.append(qn.right)
            return True
        q = [root]
        while q:
            node = q.pop()
            if isSameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
