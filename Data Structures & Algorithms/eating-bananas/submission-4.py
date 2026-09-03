class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_before(rate):
            k = 0
            for pile in piles:
                k += pile // rate + (1 if pile % rate > 0 else 0)
            return True if k > h else False
        l, r = 0, max(piles)
        while r - l > 1:
            mid = (r + l) // 2
            if is_before(mid):
                l = mid
            else:
                r = mid
        return r