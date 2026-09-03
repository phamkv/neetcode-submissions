class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False for _ in range(len(s)+1)]
        cache[-1] = True
        for i in range(len(s)+1, -1, -1):
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                    if cache[i+len(word)] == True:
                        cache[i] = True
        return cache[0]
