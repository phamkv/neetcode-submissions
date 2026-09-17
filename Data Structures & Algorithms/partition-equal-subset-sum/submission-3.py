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
            if i >= len(nums):
                return False
            for j in range(i+1, len(nums)):
                newSum = curSum + nums[j]
                if newSum <= half:
                    memo[(i, curSum)] = dfs(j, newSum)
                    if memo[(i, curSum)]:
                        return True
            memo[(i, curSum)] = dfs(i+1, curSum)
            return memo[(i, curSum)]
        return dfs(0, nums[0])