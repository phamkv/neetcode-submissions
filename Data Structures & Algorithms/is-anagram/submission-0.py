class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for c in s:
            if c in sMap:
                sMap[c] += 1
            else:
                sMap[c] = 1
        for c in t:
            if c in sMap:
                sMap[c] -= 1
                if sMap[c] == 0:
                    del sMap[c]
            else:
                return False
        if not sMap.keys():
            return True
        else:
            return False