# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        columnMap = {}
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            if col not in columnMap:
                columnMap[col] = []
            columnMap[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
        leftmost = min(columnMap.keys())
        rightmost = max(columnMap.keys())
        result = []
        for i in range(leftmost, rightmost + 1, 1):
            result.append(columnMap[i])
        return result