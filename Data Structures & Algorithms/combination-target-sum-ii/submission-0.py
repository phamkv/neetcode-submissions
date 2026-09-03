class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        seen = set()
        result = []
        q = deque([([], 0, 0)])
        while q:
            combi, val, i = q.popleft()
            for j in range(i, len(candidates)):
                num = candidates[j]
                newCombi = combi + [num]
                if num + val == target and tuple(newCombi) not in seen:
                    result.append(newCombi)
                    seen.add(tuple(newCombi))
                elif num + val < target:
                    q.append((newCombi, num + val, j+1))
        return result