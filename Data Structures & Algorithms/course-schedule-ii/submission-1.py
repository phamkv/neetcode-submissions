class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for crs, preq in prerequisites:
            adj[crs].append(preq)

        result = []
        added = set()
        visited = set()
        def dfs(crs):
            visited.add(crs)
            for preq in adj[crs]:
                if preq in visited:
                    return False
                possible = dfs(preq)
                if not possible:
                    return False
            if crs not in added:
                result.append(crs)
                added.add(crs)
            adj[crs] = []
            visited.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result
        