class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[a].append(b)

        visited = set()
        def dfs(crs):
            for preq in adj[crs]:
                if preq in visited:
                    return False
                visited.add(preq)
                if not dfs(preq):
                    return False
                visited.remove(preq)
            adj[crs] = []
            return True
            
        for i in range(numCourses):
            visited.add(i)
            if not dfs(i):
                return False
            visited.remove(i)
        return True