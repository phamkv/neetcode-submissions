class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pAscend = [1 for _ in range(len(nums) + 2)]
        pDescend = [1 for _ in range(len(nums) + 2)]
        for i in range(len(nums)):
            pAscend[i+1] = nums[i] * pAscend[i]
        for i in range(len(nums) -1, -1, -1):
            pDescend[i+1] = nums[i] * pDescend[i+2]
        res = []
        for i in range(1, len(nums) + 1):
            res.append(pAscend[i-1] * pDescend[i+1])
        return res