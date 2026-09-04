# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def ancestor(node, p, q):
            if node.val > p and node.val > q:
                return ancestor(node.left, p, q)
            elif node.val < p and node.val < q:
                return ancestor(node.right, p, q)
            return node
        return ancestor(root, p.val, q.val)