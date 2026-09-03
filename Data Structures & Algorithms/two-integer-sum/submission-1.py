class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in pos:
                return [pos[diff], i]
            pos[num] = i
            