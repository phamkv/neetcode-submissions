class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(c: str) -> bool:
            return True if ord("A") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9") else False
            
        l = 0
        r = len(s) - 1
        while l < r:
            if not isAlpha(s[l]):
                l += 1
            elif not isAlpha(s[r]):
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True