class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = max(len(word) for word in wordSet)

        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for j in range(i, min(len(s), i+t)):
                if s[i:j+1] in wordSet and dp[j+1]:
                    dp[i] = True
        return dp[0]