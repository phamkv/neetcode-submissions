class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] in wordSet and dp[i+len(word)]:
                    dp[i] = True
                    break
        return dp[0]