class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 1
        r = len(numbers)
        while l < r:
            pointerSum = numbers[l-1] + numbers[r-1]
            if pointerSum == target:
                return [l,r]
            elif pointerSum < target:
                l += 1
            else:
                r -= 1
        