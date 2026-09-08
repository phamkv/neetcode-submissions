class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        visited = set()
        def isValid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and (r,c) not in visited

        queue = deque([])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                    visited.add((r,c))
                    queue.append((r,c))
        while queue:
            r,c = queue.popleft()
            for dir_r,dir_c in directions:
                n_r,n_c = r+dir_r,c+dir_c
                if isValid(n_r,n_c) and heights[n_r][n_c] >= heights[r][c]:
                    pacific.add((n_r,n_c))
                    visited.add((n_r,n_c))
                    queue.append((n_r,n_c))
        
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS-1 or c == COLS-1:
                    atlantic.add((r,c))
                    visited.add((r,c))
                    queue.append((r,c))
        while queue:
            r,c = queue.popleft()
            for dir_r,dir_c in directions:
                n_r,n_c = r+dir_r,c+dir_c
                if isValid(n_r,n_c) and heights[n_r][n_c] >= heights[r][c]:
                    atlantic.add((n_r,n_c))
                    visited.add((n_r,n_c))
                    queue.append((n_r,n_c))
        
        result = []
        for x,y in pacific:
            if (x,y) in atlantic:
                result.append([x,y])
        return result
