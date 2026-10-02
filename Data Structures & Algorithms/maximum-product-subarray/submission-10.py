class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane
        # when to start anew
        # for max, when we are still negative
        # for min, when we still positive
        # both cases take nums if we multiply by 0
        result = nums[0]
        currMax = currMin = 1
        for num in nums:
            p1 = num * currMax
            p2 = num * currMin
            currMax = max(p1, p2, num)
            currMin = min(p1, p2, num)
            result = max(result, currMax)
        return result

