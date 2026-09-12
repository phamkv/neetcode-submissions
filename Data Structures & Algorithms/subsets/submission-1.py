class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def visit(i):
            if i == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[i])
            visit(i+1)
            subset.pop()
            visit(i+1)
        visit(0)
        return result