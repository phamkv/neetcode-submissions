class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1 for _ in range(len(nums)+1)]
        def dp(i):
            if i >= len(nums):
                return 0
            if cache[i] > -1:
                return cache[i]
            cache[i] = max(nums[i] + dp(i+2), dp(i+1))
            return cache[i]
        dp(0)
        return cache[0]