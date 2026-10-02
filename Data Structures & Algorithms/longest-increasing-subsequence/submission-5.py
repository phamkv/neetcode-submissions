from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary search with array to keep track
        # if a number is bigger than the last tracked, append it (make subsequence longer)
        # if not, replace the smallest tracked that is bigger than number
        # tracked may not be valid subsequence, but it doesnt matter: if the next one is larger, we would just think that replacing back is valid
        # nums=[10, 9, 2, 5, 3, 7, 101, 6, 102]
        if not nums:
            return 0
        incSeq = [nums[0]]
        for i in range(1, len(nums)):
            if incSeq[-1] < nums[i]:
                incSeq.append(nums[i])
                continue
            toReplace = bisect_left(incSeq, nums[i])
            incSeq[toReplace] = nums[i]
        return len(incSeq)
