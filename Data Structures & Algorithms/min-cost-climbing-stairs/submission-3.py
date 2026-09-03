class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1 for _ in range(len(cost)+1)]
        def dp(i):
            if i >= len(cost):
                return 0
            if cache[i] > -1:
                return cache[i]
            cache[i] = min(dp(i+1) + cost[i], dp(i+2) + cost[i])
            return cache[i]
        dp(0)
        dp(1)
        return min(cache[0], cache[1])