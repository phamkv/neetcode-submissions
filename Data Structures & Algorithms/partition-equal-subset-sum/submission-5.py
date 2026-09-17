class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums) // 2
        # backtracking with possible caching
        memo = {}
        def dfs(i, curSum):
            if curSum == half:
                return True
            if curSum > half:
                return False
            if i >= len(nums):
                return False
            memo[(i, curSum)] = dfs(i+1, curSum+nums[i]) or dfs(i+1, curSum)
            return memo[(i, curSum)]
        return dfs(0, 0)