class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        # floor: cost to reach the top from that floor
        def dp(floor):
            if floor == len(cost) - 1 or floor == len(cost) - 2:
                return cost[floor]
            if floor in memo:
                return memo[floor]
            memo[floor] = min(dp(floor+1), dp(floor+2)) + cost[floor]
            return memo[floor]
        return min(dp(0), dp(1))