class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r
        while l <= r:
            mid = (l+r)//2
            total = 0
            for pile in piles:
                total += pile//mid + (pile%mid > 0)
            if total <= h:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        return result