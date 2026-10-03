class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        distance = {}
        def isValid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 2147483647

        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            r,c = q.popleft()
            for dir_r, dir_c in directions:
                n_r, n_c = r+dir_r, c+dir_c
                if isValid(n_r, n_c):
                    grid[n_r][n_c] = grid[r][c] + 1
                    q.append((n_r,n_c))