# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        qq = [root]
        while q:
            node = qq.pop()
            if node.val > p.val and node.val > q.val:
                qq.append(node.left)
            elif node.val < p.val and node.val < q.val:
                qq.append(node.right)
            else:
                return node

