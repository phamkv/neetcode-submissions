class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def is_before(s, shorter, longer):
            half = (len(shorter) + len(longer)) // 2
            if s == 0:
                return longer[half-1] > shorter[0]
            elif half - s < 1:
                return shorter[s-1] > longer[0]
            else:
                left_max = max(longer[half-s-1], shorter[s-1])
                right_min = min(longer[half-s], shorter[s])
                return left_max > right_min

        shorter, longer = nums1, nums2
        if len(nums1) > len(nums2):
            shorter, longer = nums2, nums1

        if len(shorter) < 1:
            half = len(longer) // 2
            return longer[half] if len(longer) % 2 == 1 else (longer[half] + longer[half-1]) / 2
            
        half = (len(shorter) + len(longer)) // 2
        l, r = 0, len(shorter)
        if not is_before(l, shorter, longer):
            r = l
        while r - l > 1:
            mid = (r + l) // 2
            if is_before(mid, shorter, longer):
                l = mid
            else:
                r = mid
        if r == 0:
            left_max = longer[half-1]
            right_min = min(longer[half], shorter[r]) if half < len(longer) else shorter[r]
        elif r == len(shorter):
            left_max = max(longer[half-r-1], shorter[r-1]) if r < half else shorter[r-1]
            right_min = longer[half-r]
        else:
            left_max = max(longer[half-r-1], shorter[r-1])
            right_min = min(longer[half-r], shorter[r])
        return right_min if (len(shorter) + len(longer)) % 2 == 1 else (right_min + left_max) / 2
        