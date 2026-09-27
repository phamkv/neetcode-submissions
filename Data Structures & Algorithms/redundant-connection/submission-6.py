class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        indegree = {}
        for u,w in edges:
            if u not in adj:
                adj[u] = []
                indegree[u] = 0
            if w not in adj:
                adj[w] = []
                indegree[w] = 0
            adj[u].append(w)
            adj[w].append(u)
            indegree[u] += 1
            indegree[w] += 1

        q = deque([])
        inCycle = set()
        for node in adj.keys():
            inCycle.add(node)
            if len(adj[node]) == 1:
                q.append(node)
        while q:
            node = q.popleft()
            indegree[node] -= 1
            inCycle.remove(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        for i in range(len(edges)-1,-1,-1):
            u,w = edges[i]
            if u in inCycle and w in inCycle:
                return [u,w]

        