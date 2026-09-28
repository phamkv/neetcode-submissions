class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, currSet):
            if len(currSet) == k:
                res.append(currSet.copy())
            if i > n:
                return
            for j in range(i, n+1):
                currSet.append(j)
                dfs(j+1, currSet)
                currSet.pop()
        dfs(1, [])
        return res