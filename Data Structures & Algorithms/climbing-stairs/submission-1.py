class Solution:
    def climbStairs(self, n: int) -> int:
        # stairs: stairs left
        memo = {}
        def dp(stairs):
            if stairs == 1:
                return 1
            if stairs == 2:
                return 2
            if stairs in memo:
                return memo[stairs]
            memo[stairs] = dp(stairs-1) + dp(stairs-2)
            return memo[stairs]
        return dp(n)
