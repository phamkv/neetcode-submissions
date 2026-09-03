class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = [False for num in nums]
        def dfs(sub):
            for i in range(len(nums)):
                if seen[i]:
                    continue
                seen[i] = True
                dfs(sub + [nums[i]])
                seen[i] = False
            if len(sub) == len(nums):
                result.append(sub)
        dfs([])
        return result
