# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        preRootIdx = 0
        def dfs(l, r):
            if l > r:
                return None
            nonlocal preRootIdx
            rootVal = preorder[preRootIdx]
            inRootIdx = indices[rootVal]
            preRootIdx += 1
            node = TreeNode(rootVal)
            node.left = dfs(l, inRootIdx - 1)
            node.right = dfs(inRootIdx + 1, r)
            return node
        return dfs(0, len(inorder) - 1)
