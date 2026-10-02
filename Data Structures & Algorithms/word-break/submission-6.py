class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = max(len(word) for word in wordSet)

        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for j in range(i, min(len(s)+1, i+t+1)):
                if s[i:j] in wordSet and dp[j]:
                    dp[i] = True
        return dp[0]