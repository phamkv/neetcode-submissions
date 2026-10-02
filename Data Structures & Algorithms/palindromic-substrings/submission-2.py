class Solution:
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            pS = "#" + "#".join(s) + "#"
            t = len(pS)
            p = [0] * t
            l = r = 0
            for i in range(t):
                if i < r:
                    mirror = r - i + l
                    p[i] = min(p[mirror], r - i)
                while i - p[i] >= 0 and i + p[i] < t and pS[i - p[i]] == pS[i + p[i]]:
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p
        p = manacher(s)
        res = 0
        for i in p:
            res += (i) // 2
        return res