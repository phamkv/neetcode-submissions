from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxF = 0
        l = r = 0
        result = 0
        while r < len(s):
            maxF = max(maxF, freq[s[r]]+1) # only relevant if that character is the most frequent character
            if r-l - maxF < k:
                freq[s[r]] += 1
                r += 1
                result = max(result, r-l)
            else:
                freq[s[l]] -= 1
                l += 1
        return result