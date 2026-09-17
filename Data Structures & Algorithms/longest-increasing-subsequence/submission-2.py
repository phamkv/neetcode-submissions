class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp(i) longest increasing starting with i
        # base i == len(nums): 0
        # recur for j from i to end: max(dp(j)) + 1
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            currBest = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    currBest = max(currBest, dp(j) + 1)
            memo[i] = currBest
            return memo[i]
        dp(0)
        return max(dp(i) for i in range(len(nums)))