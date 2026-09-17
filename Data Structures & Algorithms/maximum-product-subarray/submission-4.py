class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = 1
        minP = 1
        result = nums[0]
        for num in nums:
            pr1 = num*maxP
            pr2 = num*minP
            maxP = max(num, pr1, pr2)
            minP = min(num, pr1, pr2)
            result = max(result, maxP, num)
        return result