class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                if not result[i]:
                    sub = [num]
                else:
                    sub = result[i].copy()
                    sub.append(num)
                result.append(sub)
        return result