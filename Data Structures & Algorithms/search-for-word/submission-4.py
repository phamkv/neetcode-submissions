class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()
        def visit(r,c,i):
            if i == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C or (r,c) in seen:
                return False
            if board[r][c] != word[i]:
                return False
            seen.add((r,c))
            for dir_r,dir_c in directions:
                n_r, n_c = r+dir_r, c+dir_c
                if visit(n_r,n_c,i+1):
                    return True
            seen.remove((r,c))
            return False
        for i in range(R):
            for j in range(C):
                if visit(i,j,0):
                    return True
        return False
            