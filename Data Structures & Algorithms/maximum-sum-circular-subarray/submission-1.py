class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxResult = -float("infinity")
        minResult = float("infinity")
        currMaxSum = 0
        currMinSum = 0
        for i in range(len(nums)):
            currMaxSum = max(currMaxSum, 0) + nums[i]
            currMinSum = min(currMinSum, 0) + nums[i]
            maxResult = max(maxResult, currMaxSum)
            minResult = min(minResult, currMinSum)
        
        return max(maxResult, sum(nums) - minResult) if maxResult > 0 else maxResult
            