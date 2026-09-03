class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowList = [set() for _ in range(9)]
        colList = [set() for _ in range(9)]
        subboxes2DList = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                value = board[i][j]
                if value == ".":
                    continue
                subbox = subboxes2DList[int(i / 3)][int(j / 3)]
                if value in rowList[i] or value in colList[j] or value in subbox:
                    return False
                rowList[i].add(value)
                colList[j].add(value)
                subbox.add(value)
        return True