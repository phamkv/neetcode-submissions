class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        arr1 = [nums[i] for i in range(len(nums)-1)]
        arr2 = [nums[i] for i in range(1, len(nums))]
        cache1 = [0 for _ in range(len(arr1))]
        cache2 = [0 for _ in range(len(arr2))]
        cache1[0] = arr1[0]
        cache1[1] = max(cache1[0], arr1[1])
        cache2[0] = arr2[0]
        cache2[1] = max(cache2[0], arr2[1])
        for i in range(2, len(arr1)):
            cache1[i] = max(cache1[i-2]+arr1[i], cache1[i-1])
            cache2[i] = max(cache2[i-2]+arr2[i], cache2[i-1])
        return max(cache1[-1], cache2[-1])