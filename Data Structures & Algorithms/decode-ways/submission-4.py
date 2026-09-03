class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [1 for _ in range(len(s)+1)]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                cache[i] = 0           
            elif i == len(s)-1:
                cache[i] = 1
            elif int(s[i]+s[i+1]) > 0 and int(s[i]+s[i+1]) <= 26:
                cache[i] = cache[i+1] + cache[i+2]
            elif s[i+1] == "0":
                return 0
            else:
                cache[i] = max(cache[i+1], cache[i+2])
        return cache[0]