class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        steps = [len(matrix[0]), len(matrix)] # COL, ROW
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        direc = 0 # COL traversal
        r = 0
        c = -1
        while steps[0] != 0 and steps[1] != 0:
            for i in range(steps[direc % 2]):
                r += directions[direc][0]
                c += directions[direc][1]
                res.append(matrix[r][c])
            if direc % 2 == 0:
                steps[1] -= 1
            else:
                steps[0] -= 1
            direc = (direc + 1) % 4
        return res