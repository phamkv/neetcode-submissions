class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftAcc = [1 for _ in range(len(nums) + 2)]
        rightAcc = [1 for _ in range(len(nums) + 2)]
        for i, num in enumerate(nums):
            leftAcc[i+1] = leftAcc[i] * num
        for i in range(len(nums) - 1, -1, -1):
            rightAcc[i+1] = rightAcc[i+2] * nums[i]
        output = []
        for i in range(len(nums)):
            result = leftAcc[i] * rightAcc[i+2]
            output.append(result)
        return output