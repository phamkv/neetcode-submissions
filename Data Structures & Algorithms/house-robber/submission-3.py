class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best1 = nums[0]
        best2 = max(best1, nums[1])
        for i in range(2, len(nums)):
            tmp = max(best1 + nums[i], best2)
            best1, best2 = best2, tmp
        return best2