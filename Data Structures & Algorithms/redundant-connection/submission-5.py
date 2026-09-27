class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for u,w in edges:
            if u not in adj:
                adj[u] = []
            if w not in adj:
                adj[w] = []
            adj[u].append(w)
            adj[w].append(u)

        visited = set()
        inCycle = set()
        cycleStart = None
        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited:
                inCycle.add(node)
                cycleStart = node
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node) and node != cycleStart:
                    inCycle.add(node)
                    return True
            return False
        dfs(edges[0][0], None)
        for i in range(len(edges)-1, -1, -1):
            u,w = edges[i]
            if u in inCycle and w in inCycle:
                return [u,w]
        
