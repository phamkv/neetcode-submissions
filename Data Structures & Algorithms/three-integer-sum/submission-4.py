class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tSum = nums[i] + nums[l] + nums[r]
                if tSum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif tSum < 0:
                    l += 1
                else:
                    r -= 1
        return res
