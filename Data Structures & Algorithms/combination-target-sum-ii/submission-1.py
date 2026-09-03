class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        q = deque([([], 0, 0)])
        while q:
            combi, val, i = q.popleft()
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                num = candidates[j]
                newCombi = combi + [num]
                if num + val == target:
                    result.append(newCombi)
                elif num + val < target:
                    q.append((newCombi, num + val, j+1))
        return result