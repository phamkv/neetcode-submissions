class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0 for _ in range(26)]
        for c in s1:
            i = ord(c) - ord('a')
            count[i] += 1
        l = r = 0
        while r < len(s2):
            i = ord(s2[r]) - ord('a')
            count[i] -= 1
            r += 1
            if r-l < len(s1):
                continue
            if min(count) == 0 and max(count) == 0:
                return True
            j = ord(s2[l]) - ord('a')
            count[j] += 1
            l += 1
        return False