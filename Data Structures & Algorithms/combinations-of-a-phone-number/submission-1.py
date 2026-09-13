class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mp = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        result = []
        sub = []
        def visit(i):
            if i == len(digits):
                result.append("".join(sub))
                return
            digit = int(digits[i])
            for letter in mp[digit]:
                sub.append(letter)
                visit(i+1)
                sub.pop()
        visit(0)
        return result