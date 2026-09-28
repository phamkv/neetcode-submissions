class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        adj = {i: [] for i in range(n)}
        for v,w in edges:
            adj[v].append(w)
            adj[w].append(v)

        seen = set()
        def dfs(node):
            seen.add(node)
            for neigh in adj[node]:
                if neigh in seen:
                    continue
                dfs(neigh)
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                result += 1
        return result + (n-len(seen))