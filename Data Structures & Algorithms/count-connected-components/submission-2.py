class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodesLeft = set([i for i in range(n)])
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
            nodesLeft.remove(node)
        
        for i in range(n):
            if i in nodesLeft:
                seen = set()
                dfs(i)
                result += 1
        return result + len(nodesLeft)