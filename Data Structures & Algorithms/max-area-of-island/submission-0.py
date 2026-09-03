class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        ROW = len(grid)
        COL = len(grid[0])
        def dfs(x,y):
            if x < 0 or x >= ROW or y < 0 or y >= COL or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)
        for i in range(ROW):
            for j in range(COL):
                area = dfs(i,j)
                result = max(result, area)
        return result