class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # freq map for letters in t -> O(52)
        # sliding window
        # mustDo if there is any freq[key] > 0 in freq.items else check length and move left border, increase freq[key] if s[l] is in freq
        # OUZODYXAZV XYZ
        # freq X0 Y0 Z0
        # OUZOD YXAZ V
        # 5 9
        if len(t) > len(s):
            return ""

        freq = {}
        for c in t:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        l = r = 0
        res = (0, len(s))
        flag = False
        while r < len(s) + 1:
            mustDo = False
            for k,v in freq.items():
                if v > 0:
                    mustDo = True
            if mustDo:
                if r < len(s):
                    if s[r] in freq:
                        freq[s[r]] -= 1
                r += 1
            else:
                flag = True
                if res[1] - res[0] > r - l:
                    res = (l,r)
                if s[l] in freq:
                    freq[s[l]] += 1
                l += 1
        return s[res[0]:res[1]] if flag else ""

        # edge cases
        # s shorter than t
        # t not possible in s
                