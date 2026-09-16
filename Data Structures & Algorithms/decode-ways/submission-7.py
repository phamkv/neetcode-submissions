class Solution:
    def numDecodings(self, s: str) -> int:
        # i number of ways in substring s[i:]
        # base s[i] == 0: 0, i == len(s) - 1: 1
        # recur dp(i+1) + dp(i+2), dp(i+1)
        memo = {}
        def dp(i):
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            if i == len(s) - 1:
                return 1
            if i == len(s) - 2:
                if int(s[i:]) <= 26:
                    memo[i] = dp(i+1) + 1
                    return memo[i]
            if int(s[i:i+2]) <= 26:
                memo[i] = dp(i+1) + dp(i+2)
                return memo[i]
            else:
                memo[i] = dp(i+1)
                return memo[i]
        return dp(0)