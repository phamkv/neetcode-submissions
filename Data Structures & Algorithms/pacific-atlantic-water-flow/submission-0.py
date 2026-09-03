class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROW = len(heights)
        COL = len(heights[0])
        def dfs(x,y, height, ocean):
            if x < 0 or x >= ROW or y < 0 or y >= COL or (x,y) in ocean or heights[x][y] < height:
                return
            ocean.add((x,y))
            dfs(x+1,y, heights[x][y], ocean)
            dfs(x-1,y, heights[x][y], ocean)
            dfs(x,y+1, heights[x][y], ocean)
            dfs(x,y-1, heights[x][y], ocean)
        for i in range(ROW):
            for j in range(COL):
                if i == 0:
                    dfs(i,j,heights[i][j],pacific)
                if j == 0:
                    dfs(i,j,heights[i][j],pacific)
                if j == COL-1:
                    dfs(i,j,heights[i][j],atlantic)
                if i == ROW-1:
                    dfs(i,j,heights[i][j],atlantic)
        result = []
        for x,y in pacific:
            if (x,y) in atlantic:
                result.append([x,y])
        return result