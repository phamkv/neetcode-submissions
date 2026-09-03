class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        mp = [[] for _ in range(n)]
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        seen = set()
        result = 0
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            for m in mp[node]:
                dfs(m)
            return True
        for i in range(n):
            if dfs(i):
                result += 1
        return result
        