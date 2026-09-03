class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            r = l
        while r - l > 1:
            mid = (r + l) // 2
            if nums[mid] > nums[len(nums)-1]:
                l = mid
            else:
                r = mid
        pivot = r
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            l, r = pivot, len(nums) - 1
        else:
            l, r = 0, pivot - 1
        if nums[l] >= target:
            r = l
        elif nums[r] < target:
            return -1
        while r - l > 1:
            mid = (r + l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r if nums[r] == target else -1
            