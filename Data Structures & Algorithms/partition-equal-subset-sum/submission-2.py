class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        t = sum(nums) // 2
        mp = {t: False}
        for i in range(len(nums)):
            num = nums[i]
            sub = []
            for j in range(1, t):
                if j in mp:
                    sub.append(j+num)
            for su in sub:
                mp[su] = True
            mp[num] = True  
        return mp[t]