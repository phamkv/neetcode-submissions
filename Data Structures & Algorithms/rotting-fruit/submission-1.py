class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mp = {}
        result = 0
        ROW = len(grid)
        COL = len(grid[0])
        def bfs(i,j):
            q = deque([(i,j,0)])
            while q:
                x,y,minute = q.popleft()
                if x < 0 or x >= ROW or y < 0 or y >= COL or grid[x][y] == 0:
                    continue
                if (x,y) in mp and mp[(x,y)] <= minute:
                    continue
                mp[(x,y)] = minute
                q.append((x+1,y,minute+1))
                q.append((x-1,y,minute+1))
                q.append((x,y+1,minute+1))
                q.append((x,y-1,minute+1))
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    bfs(i,j)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    if (i,j) not in mp:
                        return -1
                    result = max(result, mp[(i,j)])
        return result