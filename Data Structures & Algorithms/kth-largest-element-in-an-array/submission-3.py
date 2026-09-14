class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l,r):
            pIndex = l
            pivot = nums[r]
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[pIndex], nums[i] = nums[i], nums[pIndex]
                    pIndex += 1
            nums[r], nums[pIndex] = nums[pIndex], nums[r]
            if len(nums) == pIndex + k:
                return nums[pIndex]
            elif len(nums) < pIndex + k:
                return quickSelect(l, pIndex-1)
            else:
                return quickSelect(pIndex+1, r)
        return quickSelect(0, len(nums)-1)