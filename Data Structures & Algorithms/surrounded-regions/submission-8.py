class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def isValid(r,c):
            return 0<=r<ROWS and 0<=c<COLS and (r,c) not in visited and board[r][c] == "O"
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        tmp = set()
        def dfs(r,c):
            for dir_r,dir_c in directions:
                n_r,n_c = r+dir_r,c+dir_c
                if isValid(n_r,n_c):
                    visited.add((n_r,n_c))
                    dfs(n_r,n_c)
                
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS -1) and board[r][c] == "O":
                    visited.add((r,c))
                    dfs(r,c)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"