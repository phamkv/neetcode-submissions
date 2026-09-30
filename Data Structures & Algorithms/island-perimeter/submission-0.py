class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        R, C = len(grid), len(grid[0])
        
        visited = set()
        def isNotValid(r,c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 1
        def dfs(r,c):
            if (r,c) in visited:
                return 0
            elif isNotValid(r,c):
                return 1
            visited.add((r,c))
            perimeter = 0
            for dir_r, dir_c in directions:
                new_r, new_c = r+dir_r, c+dir_c
                perimeter += dfs(new_r, new_c)
            return perimeter
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return dfs(r,c)
        