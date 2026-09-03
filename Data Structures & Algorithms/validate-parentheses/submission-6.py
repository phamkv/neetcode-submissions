class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parans = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue
            if not stack or stack.pop() != parans[c]:
                return False
        return True if len(stack) == 0 else False