class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = []
        cache.append(nums[0])
        for i in range(1,len(nums)):
            if cache[-1] < nums[i]:
                cache.append(nums[i])
            else:
                l = 0
                r = len(cache)
                while l <= r:
                    mid = (r+l)//2
                    if nums[i] > cache[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                cache[l] = nums[i]
        return len(cache)