class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp(i): can substring[i:] be split into words
        # base i >= len(s): True
        # recurrent: if a word matches s[i:len(word)]: j = i + len(word), memo[i] = dp(j)
        memo = {}
        def dp(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]
            memo[i] = False
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    canDo = dp(i+len(word))
                    if canDo:
                        memo[i] = canDo
                        return memo[i]
            return memo[i]
        return dp(0)
            