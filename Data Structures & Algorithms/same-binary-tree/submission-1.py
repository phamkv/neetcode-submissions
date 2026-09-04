# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQ = deque([p])
        qQ = deque([q])
        while pQ and qQ:
            pNode = pQ.pop()
            qNode = qQ.pop()
            if pNode and qNode and pNode.val == qNode.val:
                pQ.append(pNode.left)
                pQ.append(pNode.right)
                qQ.append(qNode.left)
                qQ.append(qNode.right)
                continue
            elif not pNode and not qNode:
                continue
            return False
        return True if not pQ and not qQ else False