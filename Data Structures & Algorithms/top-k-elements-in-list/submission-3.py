class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = [[] for _ in range(len(nums)+1)]
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for key,v in count.items():
            group[v].append(key)
        res = []
        j = 0
        for i in range(len(group) - 1, -1, -1):
            if j == k:
                break
            if not group[i]:
                continue
            for num in group[i]:
                res.append(num)
                j += 1
                if j == k:
                    break
        return res

