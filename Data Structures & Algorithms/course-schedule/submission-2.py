class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {}
        tmp = set()
        seen = set()
        for a,b in prerequisites:
            if a not in mp:
                mp[a] = []
            mp[a].append(b)
        def dfs(a):
            if a in tmp:
                print(a)
                return False
            seen.add(a)
            tmp.add(a)
            if a in mp:
                for pre in mp[a]:
                    if not dfs(pre):
                        return False
            tmp.remove(a)
            return True
        for a, _ in mp.items():
            if a in seen:
                continue
            if not dfs(a):
                return False
        return True

