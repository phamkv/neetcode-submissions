class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # can we do a sum for given s
        if sum(nums) % 2:
            return False
        half = sum(nums) // 2
        dp = [False] * (half + 1)
        dp[0] = True
        for num in nums:
            toAdd = [i for i in range(half+1) if dp[i]]
            for s in toAdd:
                if s+num <= half:
                    dp[s+num] = True
        return dp[half]
        