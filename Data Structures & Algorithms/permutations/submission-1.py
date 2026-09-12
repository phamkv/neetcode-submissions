class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = nums.copy()
        result = []
        def visit(i):
            if i == len(nums) - 1:
                result.append(perm[:])
                return
            for j in range(i,len(nums)):
                perm[i], perm[j] = perm[j], perm[i]
                visit(i+1)
                perm[i], perm[j] = perm[j], perm[i]
        visit(0)
        return result
            