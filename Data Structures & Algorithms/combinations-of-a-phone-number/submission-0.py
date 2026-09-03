class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        tmp = []
        mp = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        def dfs(i):
            if i == len(digits):
                result.append("".join(tmp))
                return
            d = int(digits[i])
            for c in mp[d]:
                tmp.append(c)
                dfs(i+1)
                tmp.pop()
        dfs(0)
        return result
            