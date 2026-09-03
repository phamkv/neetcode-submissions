class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        while l < r:
            mid = (l+r)//2
            print(mid)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]
        
            