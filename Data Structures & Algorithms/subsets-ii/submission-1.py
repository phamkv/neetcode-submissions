class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def visit(i):
            if i == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[i])
            visit(i+1)
            subset.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            visit(i+1)
        visit(0)
        return result