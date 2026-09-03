"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}
        if not node:
            return
        def dfs(node):
            if node in mp:
                return
            mp[node] = Node(node.val)
            for neighbor in node.neighbors:
                dfs(neighbor)
                mp[node].neighbors.append(mp[neighbor])
        dfs(node)
        return mp[node]