class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        best1 = nums[0]
        best2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = best1
            best1 = best2
            best2 = max(tmp + nums[i], best2)
        return best2

        