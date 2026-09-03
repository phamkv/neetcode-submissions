class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freqMap = {}
        maxF = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in freqMap:
                freqMap[s[r]] = 0
            freqMap[s[r]] += 1
            maxF = max(maxF, freqMap[s[r]])
            while r - l + 1 - maxF > k:
                freqMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res