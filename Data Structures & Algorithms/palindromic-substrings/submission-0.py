class Solution:
    def countSubstrings(self, s: str) -> int:
        # Two Pointer braucht weniger Space
        result = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                result += 1
                l -= 1
                r += 1
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                result += 1
                l -= 1
                r += 1
        return result