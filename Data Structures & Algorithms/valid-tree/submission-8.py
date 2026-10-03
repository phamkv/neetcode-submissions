class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = {i: [] for i in range(n)}
        for v,w in edges:
            adj[v].append(w)
            adj[w].append(v)

        seen = set([0])
        q = deque([0])
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        return len(seen) == n