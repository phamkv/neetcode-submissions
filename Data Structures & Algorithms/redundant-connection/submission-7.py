class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for u,w in edges:
            if u not in adj:
                adj[u] = set()
            if w not in adj:
                adj[w] = set()
            adj[u].add(w)
            adj[w].add(u)

        q = deque([])
        inCycle = set()
        for node in adj.keys():
            inCycle.add(node)
            if len(adj[node]) == 1:
                q.append(node)
        while q:
            node = q.popleft()
            inCycle.remove(node)
            for nei in adj[node]:
                adj[nei].remove(node)
                if len(adj[nei]) == 1:
                    q.append(nei)
        for i in range(len(edges)-1,-1,-1):
            u,w = edges[i]
            if u in inCycle and w in inCycle:
                return [u,w]

        