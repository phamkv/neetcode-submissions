class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            best = dp[i]
            for j in range(i, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                best = max(best, 1 + dp[j])
            dp[i] = best
        return max(dp)