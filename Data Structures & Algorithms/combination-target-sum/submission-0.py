class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        seen = set()
        q = deque([([], 0, 0)])
        while q:
            combi, val, i = q.popleft()
            for j in range(i, len(nums)):
                num = nums[j]
                newCombi = combi + [num]
                if val + num == target:
                    result.append(newCombi)
                elif val + num < target:
                    q.append((newCombi, val + num, j))
        return result