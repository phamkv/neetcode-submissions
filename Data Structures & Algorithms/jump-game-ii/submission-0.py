class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        count = 0
        while r < len(nums) - 1:
            bestJump = 0
            for i in range(l, r+1):
                if r >= len(nums):
                    continue
                bestJump = max(bestJump, i + nums[i])
            l = r + 1
            r = bestJump
            count += 1
        return count