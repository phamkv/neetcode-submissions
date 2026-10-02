class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        best1 = best2 = 0
        for i in range(2, len(cost)):
            minCost = min(best1 + cost[i-2], best2 + cost[i-1])
            best1, best2 = best2, minCost
        return min(best1 + cost[-2], best2 + cost[-1])