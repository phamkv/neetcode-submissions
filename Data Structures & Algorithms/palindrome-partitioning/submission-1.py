class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        result = []
        sub = []
        def visit(i,j):
            if i == len(s):
                result.append(sub[:])
                return
            if j == len(s):
                return

            if isPalindrome(i,j):
                sub.append(s[i:j+1])
                visit(j+1,j+1)
                sub.pop()

            visit(i,j+1)
        visit(0,0)
        return result
            
            

            