class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp(i, started) best subarray sum starting from i given if there has been a current subarray running or not
        # base i == len(nums) - 1, false: include. true: include or not
        # recurrent false: nums[i] + dp(i+1,true), true: max(nums[i] + dp(i+1,true), dp(i+1,false))
        memo = {}
        def dp(i, running):
            if i == len(nums) - 1:
                memo[(i, running)] = max(0, nums[i]) if running else nums[i]
                return memo[(i, running)]
            if (i, running) in memo:
                return memo[(i, running)]
            if running:
                memo[(i, running)] = max(nums[i] + dp(i+1, True), nums[i])
            else:
                memo[(i, running)] = max(nums[i] + dp(i+1, True), dp(i+1, False))
            return memo[(i, running)]
        dp(0, False)
        return memo[(0, False)]
