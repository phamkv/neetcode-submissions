class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if not prices:
            return res
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            res = max(res, prices[i] - lowest)
        return res