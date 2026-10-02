class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = defaultdict(dict)
        resIndex = 0
        resLen = 0
        def dp(l,r):
            nonlocal resIndex, resLen
            if s[l] == s[r] and (r - l < 2 or memo[l+1][r-1]):
                memo[l][r] = True
                if resLen < r-l+1:
                    resIndex = l
                    resLen = r-l+1
            else:
                memo[l][r] = False
        for i in range(len(s)):
            for j in range(i, -1, -1):
                dp(j,i)
        return s[resIndex:resIndex+resLen]
                
        