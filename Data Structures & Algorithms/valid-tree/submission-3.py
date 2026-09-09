class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        adj = {i: [] for i in range(n)}
        for v,w in edges:
            adj[v].append(w)
            adj[w].append(v)
        seen = set()
        def dfs(node,parent):
            seen.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if neigh in seen:
                    return False
                if not dfs(neigh,node):
                    return False
            return True
        if not dfs(edges[0][0], None):
            return False
        return len(seen) == n