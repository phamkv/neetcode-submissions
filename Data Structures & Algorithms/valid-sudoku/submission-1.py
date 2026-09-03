class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for x in range(len(board)):
            for y in range(len(board[0])):
                entry = board[x][y]
                if entry == ".":
                    continue
                if entry in rows[x] or entry in cols[y] or entry in boxes[int(x/3)][int(y/3)]:
                    return False
                rows[x].add(entry)
                cols[y].add(entry)
                boxes[x//3][y//3].add(entry)
        return True