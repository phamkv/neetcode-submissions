class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()
        def visit(r,c,i):
            if i == len(word) - 1:
                return True
            
            for dir_r,dir_c in directions:
                n_r, n_c = r+dir_r, c+dir_c
                if n_r < 0 or n_r >= R or n_c < 0 or n_c >= C or (n_r,n_c) in seen or board[n_r][n_c] != word[i+1]:
                    continue
                seen.add((n_r, n_c))
                if visit(n_r,n_c,i+1):
                    return True
                seen.remove((n_r, n_c))
            return False
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    seen.add((i,j))
                    if visit(i,j,0):
                        return True
                    seen.remove((i,j))
        return False
            