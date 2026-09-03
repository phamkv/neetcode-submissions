class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not self.isAlphaNumeric(s[l]):
                l += 1
                continue
            elif not self.isAlphaNumeric(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def isAlphaNumeric(self, c):
        if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
            return True
        else: return False