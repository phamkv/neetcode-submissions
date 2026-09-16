class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        exLast = nums.copy()
        exLast[-1] = 0
        
        memo = {}
        def dp(i, houses):
            if i >= len(houses):
                return 0
            if (i, houses) in memo:
                return memo[(i, houses)]
            memo[(i, houses)] = max(houses[i] + dp(i+2, houses), dp(i+1, houses))
            return memo[(i, houses)]
        return max(dp(0, tuple(exLast)), dp(1, tuple(nums)))
