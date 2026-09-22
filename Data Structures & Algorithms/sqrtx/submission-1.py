class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        #binary search
        #biggest number i so that i * i <= x
        l = 0
        r = x
        while r - l > 1:
            mid = (r + l) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid
        return l