class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        sub = []
        def visit(o,c):
            if o == c == n:
                result.append("".join(sub))
            if o < n:
                sub.append('(')
                visit(o+1,c)
                sub.pop()
            if c < o:
                sub.append(')')
                visit(o,c+1)
                sub.pop()
        visit(0,0)
        return result