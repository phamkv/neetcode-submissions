class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def numOfWays(i):
            if i == len(s):
                return 1
            elif s[i] == "0":
                return 0
            elif i == len(s) - 1:
                return 1
            if i in memo:
                return memo[i]
            elif 10 <= int(s[i:i+2]) <= 26:
                memo[i] = numOfWays(i+1) + numOfWays(i+2)
            else:
                memo[i] = numOfWays(i+1)
            return memo[i]
        return numOfWays(0)