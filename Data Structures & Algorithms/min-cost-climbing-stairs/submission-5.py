class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)
        dp[-1] = dp[-2] = 0
        for i in range(len(cost)-1, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        return min(dp[0], dp[1]) if len(cost) > 1 else dp[0]