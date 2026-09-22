class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search
        #biggest number i so that i * i <= x
        l = 0
        r = x
        if r * r <= x:
            return r
        while r - l > 1:
            mid = (r + l) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid
        return l