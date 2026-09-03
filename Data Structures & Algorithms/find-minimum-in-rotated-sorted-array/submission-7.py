class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r - l > 1:
            mid = (r + l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return nums[l] if nums[l] < nums[r] else nums[r]