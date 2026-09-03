class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        if n == 1:
            return True
        seen = set()
        mp = {}
        for a,b in edges:
            if a not in mp:
                mp[a] = []
            if b not in mp:
                mp[b] = []
            mp[a].append(b)
            mp[b].append(a)
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for m in mp[node]:
                dfs(m)
        dfs(edges[0][0])
        if len(seen) == n:
            return True
        return False
                