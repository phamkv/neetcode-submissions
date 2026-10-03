class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        distance = [[0] * COLS for _ in range(ROWS)]
        def isValid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and grid[r][c] == 1 and distance[r][c] == 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    distance[r][c] = 0
        
        while q:
            r,c = q.popleft()
            for dirR, dirC in directions:
                nR, nC = r+dirR, c+dirC
                if isValid(nR, nC):
                    distance[nR][nC] = distance[r][c] + 1
                    q.append((nR,nC))
        
        result = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and distance[r][c] == 0:
                    return -1
                result = max(result, distance[r][c])
        return result

        