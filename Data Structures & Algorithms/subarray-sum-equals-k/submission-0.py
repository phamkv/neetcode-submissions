class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefixSum[i] = nums[i]
            else:
                prefixSum[i] = prefixSum[i-1] + nums[i]
        #two diff sum with prefixSum
        mp = defaultdict(int)
        mp[0] = 1
        result = 0
        for i in range(len(prefixSum)):
            diff = prefixSum[i] - k
            result += mp[diff]
            mp[prefixSum[i]] += 1
        return result