class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        best1, best2 = cost[-1], cost[-2]
        for i in range(len(cost)-3, -1, -1):
            minCost = min(best1, best2) + cost[i]
            best1, best2 = best2, minCost
        return min(best1, best2)