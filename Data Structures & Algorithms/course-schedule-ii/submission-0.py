class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        seen = set()
        mp = {}
        for a,b in prerequisites:
            if a not in mp:
                mp[a] = set()
            mp[a].add(b)
        q = deque([])
        for i in range(numCourses):
            if i not in mp:
                q.append(i)
        while q:
            course = q.popleft()
            for a,preqs in mp.items():
                if course in preqs:
                    preqs.remove(course)
                    if len(preqs) == 0:
                        q.append(a)
            result.append(course)
        return result if len(result) == numCourses else []