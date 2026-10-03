class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # beware of n
        adj = collections.defaultdict(list)
        for u, w in edges:
            adj[u].append(w)
            adj[w].append(u)
        
        nodeToCC = {}
        def bfs(node, cc):
            q = collections.deque([node])
            nodeToCC[node] = cc
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in nodeToCC:
                        nodeToCC[nei] = cc
                        q.append(nei)
        
        ccId = 0
        for node in adj.keys():
            if node not in nodeToCC:
                ccId += 1
                bfs(node, ccId)
        return ccId + n - len(adj)
