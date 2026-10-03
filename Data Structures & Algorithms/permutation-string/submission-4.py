class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = defaultdict(int)
        for c in s1:
            count[c] += 1
        missing = len(count)
        l = r = 0
        while r < len(s2):
            count[s2[r]] -= 1
            if count[s2[r]] == 0:
                missing -= 1
            r += 1
            if r >= len(s1):
                if missing == 0:
                    return True
                count[s2[l]] += 1
                if count[s2[l]] == 1:
                    missing += 1
                l += 1
        return False