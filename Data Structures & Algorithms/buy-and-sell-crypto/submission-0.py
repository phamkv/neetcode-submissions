class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l = 0
        r = 1
        while r < len(prices) and l < r:
            if prices[l] >= prices[r]:
                l += 1
                r += 1
            else:
                while r < len(prices) and prices[l] < prices[r]:
                    result = max(result, prices[r] - prices[l])
                    r += 1
                l = r - 1
        return result