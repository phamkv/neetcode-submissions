class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        def bfs(i,j):
            q = deque([(i,j,0)])
            while q:
                x,y,dist = q.popleft()
                if x < 0 or x >= ROW or y < 0 or y >= COL or grid[x][y] == -1 or grid[x][y] < dist:
                    continue
                grid[x][y] = dist
                q.append((x+1,y,dist+1))
                q.append((x-1,y,dist+1))
                q.append((x,y+1,dist+1))
                q.append((x,y-1,dist+1))
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    bfs(i,j)