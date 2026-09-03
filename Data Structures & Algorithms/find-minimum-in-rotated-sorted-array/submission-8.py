class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            r = l
        while r - l > 1:
            mid = (r + l) // 2
            if nums[mid] > nums[len(nums)-1]:
                l = mid
            else:
                r = mid
        return nums[r]