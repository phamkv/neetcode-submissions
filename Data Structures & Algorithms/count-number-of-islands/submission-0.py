class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        result = 0
        def dfs(x,y):
            if (x,y) in seen or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == "0":
                return False
            seen.add((x,y))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j):
                    result += 1
        return result