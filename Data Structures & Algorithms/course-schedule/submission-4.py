class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            adj[crs].append(preq)
        
        path = set()
        seen = set()
        def dfs(crs):
            if crs in path:
                return False
            if crs in seen:
                return True
            seen.add(crs)
            path.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            path.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True