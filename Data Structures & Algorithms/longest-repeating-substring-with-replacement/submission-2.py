class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxF = 0
        l = r = 0
        result = 0
        while r < len(s):
            maxF = max(maxF, freq.get(s[r],0)+1)
            if maxF + k > r-l:
                if s[r] not in freq:
                    freq[s[r]] = 0
                freq[s[r]] += 1
                r += 1
                result = max(result, r-l)
            else:
                freq[s[l]] -= 1
                l += 1
        return result