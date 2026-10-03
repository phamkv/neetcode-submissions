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

        freq = defaultdict(int)
        for c in t:
            freq[c] += 1
        missing = len(freq.keys())
        l = r = 0
        res = (-1, -1)
        while True:
            mustDo = missing > 0
            if mustDo:
                if r == len(s):
                    break
                if s[r] in freq:
                    freq[s[r]] -= 1
                    if freq[s[r]] == 0:
                        missing -= 1
                r += 1
            else:
                if res[0] == -1 or res[1] - res[0] > r - l:
                    res = (l,r)
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] == 1:
                        missing += 1
                l += 1
        return s[res[0]:res[1]] if res[0] != -1 else ""

        # edge cases
        # s shorter than t
        # t not possible in s
        # after adding s[-1] to window, keep checking
                