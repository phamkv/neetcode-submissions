class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0 for _ in range(n+1)]
        def dp(i):
            if i <= n and cache[i] > 0:
                return cache[i]
            if i > n:
                return 0
            if i == n:
                return 1
            val1 = dp(i+1)
            val2 = dp(i+2)
            cache[i] = val1+val2
            return cache[i]
        return dp(0)
        