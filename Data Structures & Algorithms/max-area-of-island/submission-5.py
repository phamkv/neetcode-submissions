class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = [[False] * COLS for _ in range(ROWS)]

        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and not seen[r][c] and grid[r][c] == 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def area(r,c):
            q = deque([(r,c)])
            seen[r][c] = True
            count = 1
            while q:
                r, c = q.popleft()
                for dir_r, dir_c in directions:
                    nR, nC = r+dir_r, c+dir_c
                    if isValid(nR, nC):
                        count += 1
                        seen[nR][nC] = True
                        q.append((nR,nC))
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if isValid(r,c):
                    size = area(r,c)
                    result = max(result, size)
        return result


