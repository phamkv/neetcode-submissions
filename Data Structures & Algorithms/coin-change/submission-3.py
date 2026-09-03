class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = [0 for _ in range(amount+1)]
        for i in range(1, amount+1):
            result = amount+1
            for coin in coins:
                if coin <= i:
                    result = min(result, cache[i - coin]+1)
            cache[i] = result
        return cache[-1] if cache[-1] < amount+1 else -1