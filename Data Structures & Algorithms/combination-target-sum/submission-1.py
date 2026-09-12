class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        comb = []
        def visit(i, currSum):
            if currSum == target:
                result.append(comb[:])
                return
            for j in range(i,len(nums)):
                if currSum+nums[j] > target:
                    continue
                comb.append(nums[j])
                visit(j, currSum+nums[j])
                comb.pop()
        visit(0,0)
        return result