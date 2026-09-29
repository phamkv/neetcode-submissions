class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                break
        pointer = 0
        while nums[pointer] != nums[slow]:
            pointer = nums[pointer]
            slow = nums[slow]
        return nums[pointer]
        