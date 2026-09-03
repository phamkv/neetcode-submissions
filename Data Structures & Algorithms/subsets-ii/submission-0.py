class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(sub, i):
            result.append(sub)
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                nSub = sub + [nums[j]]
                dfs(nSub, j+1)
        dfs([],0)
        return result
