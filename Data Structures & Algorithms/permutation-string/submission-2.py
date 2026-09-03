class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqMap = {}
        for i in range(len(s1)):
            if s1[i] not in freqMap:
                freqMap[s1[i]] = 0
            freqMap[s1[i]] += 1
        l = 0
        for r in range(len(s2)):
            if not freqMap:
                return True
            freqMap[s2[r]] = freqMap.get(s2[r], 0) - 1
            if freqMap[s2[r]] == 0:
                del freqMap[s2[r]]
            while r - l + 1 > len(s1):
                freqMap[s2[l]] = freqMap.get(s2[l], 0) + 1
                if freqMap[s2[l]] == 0:
                    del freqMap[s2[l]]
                l += 1
        return True if not freqMap else False