class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = [[False] * COLS for _ in range(ROWS)]

        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and not seen[r][c] and grid[r][c] == 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def area(r, c):
            count = 1
            for dir_r, dir_c in directions:
                n_r, n_c = r + dir_r, c + dir_c
                if isValid(n_r, n_c):
                    seen[n_r][n_c] = True
                    count += area(n_r, n_c)
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if isValid(r, c):
                    seen[r][c] = True
                    size = area(r, c)
                    result = max(result, size)
        return result
