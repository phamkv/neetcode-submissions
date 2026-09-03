class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distincts = set(nums)
        result = 0
        for num in nums:
            if num-1 in distincts:
                continue
            seqLen = 1
            nextNum = num + 1
            while nextNum in distincts:
                seqLen += 1
                nextNum += 1
            result = max(result, seqLen)
        return result