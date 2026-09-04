class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r,c) not in seen and grid[r][c] == "1"
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()
        result = 0
        def dfs(r,c):
            if isValid(r,c):
                seen.add((r,c))
                for i, j in directions:
                    dfs(r+i, c+j)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if isValid(r,c):
                    result += 1
                dfs(r,c)
        return result        