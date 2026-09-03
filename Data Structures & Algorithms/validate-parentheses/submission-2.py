class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")": "(", "}" : "{", "]": "["}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack or match[c] != stack.pop():
                    return False
        if stack:
            return False
        return True
        