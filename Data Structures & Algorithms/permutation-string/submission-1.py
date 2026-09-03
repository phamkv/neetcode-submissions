class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            count[c] = 1 + count.get(c, 0)
        l = 0
        for r in range(len(s2)):
            if not count:
                return True
            count[s2[r]] = -1 + count.get(s2[r], 0)
            if count[s2[r]] == 0:
                del count[s2[r]]
            if r < len(s1):
                continue
            count[s2[l]] = 1 + count.get(s2[l], 0)
            if count[s2[l]] == 0:
                del count[s2[l]]
            l += 1
        if not count:
                return True
        return False