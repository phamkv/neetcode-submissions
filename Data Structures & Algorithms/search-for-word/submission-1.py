class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        self.result = False
        h, w = len(board)-1, len(board[0])-1
        def dfs(chain, x, y, i):
            if x < 0 or x > w or y < 0 or y > h or i >= len(word) or (x,y) in seen or board[y][x] != word[i]:
                return
            c = board[y][x]
            chain = chain + c
            if chain == word:
                self.result = True
                return
            seen.add((x,y))
            dfs(chain, x+1, y, i+1)
            dfs(chain, x-1, y, i+1)
            dfs(chain, x, y+1, i+1)
            dfs(chain, x, y-1, i+1)
            seen.remove((x,y))
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs("", j, i, 0)
        return self.result