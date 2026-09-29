from collections import deque

class MaxQueue:
    def __init__(self):
        self.queue = deque([])
    
    def append(self, val):
        while self.queue and self.queue[-1] < val:
            self.queue.pop()
        self.queue.append(val)
    
    def top(self):
        return self.queue[0] if self.queue else None

    def remove(self):
        if not self.queue:
            return
        self.queue.popleft()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # slide window of size k through nums
        # each time, iterate through window and find amx
        # store that value in result array
        # O(n*k)
        # monotonic descending queue keeps track of biggest number and next biggest number after that.
        maxQ = MaxQueue()
        res = []
        l = r = 0
        while r < len(nums):
            if r + 1 < k:
                maxQ.append(nums[r])
                r += 1
            else:
                maxQ.append(nums[r])
                res.append(maxQ.top())
                if nums[l] == maxQ.top():
                    maxQ.remove()
                l += 1
                r += 1
        return res


        