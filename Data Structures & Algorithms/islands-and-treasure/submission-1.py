class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        distance = {}
        def isvalid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] != -1 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    distance[(i,j)] = 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque([key for key,val in distance.items()])
        while q:
            r,c = q.popleft()
            dist = distance[(r,c)] + 1
            for dir_r, dir_c in directions:
                n_r, n_c = r+dir_r, c+dir_c
                if isvalid(n_r, n_c):
                    if (n_r,n_c) in distance and distance[(n_r,n_c)] <= dist:
                        continue
                    distance[(n_r,n_c)] = dist
                    grid[n_r][n_c] = dist
                    q.append((n_r,n_c))


