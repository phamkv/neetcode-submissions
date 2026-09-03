class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(parans, opened, closed):
            if opened == closed == n:
                result.append(parans)
            if closed < opened:
                dfs(parans + ")", opened, closed+1)
            if opened < n:
                dfs(parans + "(", opened+1, closed)
        dfs("", 0, 0)
        return result