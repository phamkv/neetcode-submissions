class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        comb = []
        def visit(i, currSum):
            if currSum == target:
                result.append(comb[:])
                return
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if currSum + candidates[j] > target:
                    continue
                comb.append(candidates[j])
                visit(j+1, currSum + candidates[j])
                comb.pop()
        visit(0,0)
        return result
                