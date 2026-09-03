class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = {}
        for a,b in edges:
            if a not in mp:
                mp[a] = a
            if b not in mp:
                mp[b] = b
        def dfs(node):
            if mp[node] == node:
                return node
            return dfs(mp[node])
        for a,b in edges:
            ra = dfs(a)
            rb = dfs(b)
            if ra == rb:
                return [a,b]
            mp[ra] = rb