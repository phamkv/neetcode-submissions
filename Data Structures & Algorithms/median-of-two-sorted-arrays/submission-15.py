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
        if len(nums1) < 1:
            half = len(nums2) // 2
            return nums2[half] if len(nums2) % 2 == 1 else (nums2[half] + nums2[half-1]) / 2
        if len(nums2) < 1:
            half = len(nums1) // 2
            return nums1[half] if len(nums1) % 2 == 1 else (nums1[half] + nums1[half-1]) / 2
            
        shorter, longer = [], []
        if len(nums1) <= len(nums2):
            shorter, longer = nums1, nums2
        else:
            shorter, longer = nums2, nums1
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
        