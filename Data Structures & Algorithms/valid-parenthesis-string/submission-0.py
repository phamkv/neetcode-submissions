class Solution:
    def checkValidString(self, s: str) -> bool:
        maxOpen = minOpen = 0
        for c in s:
            if c == "(":
                maxOpen += 1
                minOpen += 1
            elif c == ")":
                maxOpen -= 1
                minOpen = max(minOpen-1, 0)
            else:
                maxOpen += 1
                minOpen = max(minOpen-1, 0)
            if maxOpen < 0:
                return False
        return minOpen == 0
            