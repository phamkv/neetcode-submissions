class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        distance = {}
        def isvalid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and grid[r][c] == 1 and (r,c) not in distance
        
        q = deque([])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    distance[(r,c)] = 0
                    q.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            for dir_r,dir_c in directions:
                n_r,n_c = r+dir_r,c+dir_c
                if isvalid(n_r,n_c):
                    distance[(n_r,n_c)] = distance[(r,c)] + 1
                    q.append((n_r,n_c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in distance:
                    return - 1
        
        return max(distance.values()) if distance.values() else 0