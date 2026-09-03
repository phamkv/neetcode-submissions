class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subs = []
        def isPali(i,j):
            l = i
            r = j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def dfs(j, i):
            if i > len(s) - 1:
                if j > len(s)-1:
                    result.append(subs.copy())
                return
            if isPali(j,i):
                subs.append(s[j:i+1])
                dfs(i+1,i+1)
                subs.pop()
            dfs(j,i+1)
        dfs(0,0)
        return result

