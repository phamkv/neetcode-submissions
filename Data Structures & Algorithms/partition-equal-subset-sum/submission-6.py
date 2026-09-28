class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        N = len(nums)
        S = sum(nums) // 2
        dp = [[False]*(S+1) for _ in range(N)]

        dp[0][nums[0]] = True

        for i in range(1, N):
            for s in range(S+1):
                skip = dp[i-1][s]
                include = False
                if s >= nums[i]:
                    include = dp[i-1][s-nums[i]]
                dp[i][s] = skip or include
        return dp[-1][-1]
                
