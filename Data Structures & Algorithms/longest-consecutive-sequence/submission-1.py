class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        lengthMap = {}
        for num in nums:
            if num in lengthMap:
                continue
            leftSeq = lengthMap.get(num-1, 0)
            rightSeq = lengthMap.get(num+1, 0)
            lengthMap[num] = leftSeq + 1 + rightSeq
            if leftSeq > 0:
                lengthMap[num-leftSeq] = lengthMap[num]
            if rightSeq > 0:
                lengthMap[num+rightSeq] = lengthMap[num]
            result = max(result, lengthMap[num])
        return result