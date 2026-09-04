class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        def isValid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in seen and grid[r][c] == 1
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if not isValid(r,c):
                return 0
            seen.add((r,c))
            area = 1
            for i,j in directions:
                area += dfs(r+i,c+j) 
            return area
        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r,c)
                result = max(result, area)
        return result