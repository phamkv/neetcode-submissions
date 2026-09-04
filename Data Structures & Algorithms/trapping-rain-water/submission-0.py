class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        result = 0
        while l < r:
            # move pointer which one has smaller max
            # moving can only be smaller than the one not moving
            # water can only be as high as max of smaller one
            # smaller bars just reduce area of water
            # higher bars than max of smaller pointer will raise water level at THAT point
            if maxL >= maxR:
                result += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
            else:
                result += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
        return result

         