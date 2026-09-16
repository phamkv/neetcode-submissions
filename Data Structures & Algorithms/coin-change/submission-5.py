class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # i least coins to amount change
        # base any coin fits perfectly for i
        # recur going through each coin
        # (i,n) target and how many coins
        if amount == 0:
            return 0
        memo = {}
        def dp(i):
            if min(coins) > i:
                return -1
            if i in memo:
                return memo[i]
            best = float("infinity")
            for coin in coins:
                if coin == i:
                    best = 0
                n = dp(i-coin)
                if n > 0:
                    best = min(best, n)
            if best == float("infinity"):
                memo[i] = -1
            else:
                memo[i] = best + 1
            return memo[i]
        return dp(amount)
            
            