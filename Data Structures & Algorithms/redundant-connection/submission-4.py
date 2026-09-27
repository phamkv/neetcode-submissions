class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def findParent(node):
            curr = node
            while parent[curr] != curr:
                curr = parent[parent[curr]]
            return curr

        parent = {}
        rank = {}
        for u,w in edges:
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if w not in parent:
                parent[w] = w
                rank[w] = 0
        for u,w in edges:
            parentU = findParent(u)
            parentW = findParent(w)
            if parentU == parentW:
                return [u,w]
            elif rank[parentW] >= rank[parentU]:
                parent[parentU] = parentW
                rank[parentW] += 1
            else:
                parent[parentW] = parentU
                rank[parentU] += 1
        