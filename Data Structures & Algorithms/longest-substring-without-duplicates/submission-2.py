class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsIn = set()
        l = r = 0
        result = 0
        while r < len(s):
            if s[r] not in charsIn:
                charsIn.add(s[r])
                r += 1
                result = max(result, r-l)
            else:
                charsIn.remove(s[l])
                l += 1
        return result