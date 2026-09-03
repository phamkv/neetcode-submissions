class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        tmp = set()
        ROW = len(board)
        COL = len(board[0])
        def dfs(x,y):
            if x < 0 or x >= ROW or y < 0 or y >= COL:
                return False
            if board[x][y] == "X" or (x,y) in tmp:
                return True
            seen.add((x,y))
            tmp.add((x,y))
            return dfs(x+1,y) and dfs(x-1,y) and dfs(x,y+1) and dfs(x,y-1)
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O" and (i,j) not in seen:
                    tmp = set()
                    srd = dfs(i,j)
                    if srd:
                        for x,y in tmp:
                            board[x][y] = "X"
        