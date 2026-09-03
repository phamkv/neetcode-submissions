class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}
        for i in range(0, len(nums), 1):
            if nums[i] in diffMap:
                return [diffMap[nums[i]], i]
            diffMap[target - nums[i]] = i
        return []