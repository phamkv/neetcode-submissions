class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        tmp = set()
        ROW = len(board)
        COL = len(board[0])
        def dfs(x,y):
            if x < 0 or x >= ROW or y < 0 or y >= COL:
                return False
            if board[x][y] == "X" or (x,y) in seen:
                return True
            seen.add((x,y))
            tmp.add((x,y))
            a = dfs(x+1,y)
            b = dfs(x-1,y)
            c = dfs(x,y+1)
            d = dfs(x,y-1)
            return a and b and c and d
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O" and (i,j) not in seen:
                    tmp = set()
                    srd = dfs(i,j)
                    if srd:
                        for x,y in tmp:
                            board[x][y] = "X"
        