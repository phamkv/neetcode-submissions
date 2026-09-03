class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        res = 0
        for num in nums:
            if num-1 in elems:
                continue
            k = 1
            while num+k in elems:
                k += 1
            res = max(res, k)
        return res