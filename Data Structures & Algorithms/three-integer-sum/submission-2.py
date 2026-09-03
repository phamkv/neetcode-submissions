class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num or i+2 == len(nums):
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                pSum = num + nums[l] + nums[r]
                if pSum == 0:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                elif pSum < 0:
                    l += 1
                else:
                    r -= 1
        return result