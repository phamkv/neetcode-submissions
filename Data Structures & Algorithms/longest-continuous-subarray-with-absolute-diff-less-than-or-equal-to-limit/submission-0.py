class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #8 4 2 6
        #8 4 10 7 8 6 2
        # we care about max -> max coming after and min -> min coming after. we can use deque to store order. we remove from deque because once we found a smaller one, we dont care about all before
        minQ = deque([])
        maxQ = deque([])
        l = 0
        r = 0
        result = 0
        while r < len(nums):
            if r - l == 0:
                minQ.append(nums[r])
                maxQ.append(nums[r])
                r += 1
            elif abs(nums[r]-minQ[0]) <= limit and abs(nums[r]-maxQ[0]) <= limit:
                while minQ and minQ[-1] > nums[r]:
                    minQ.pop()
                while maxQ and maxQ[-1] < nums[r]:
                    maxQ.pop()
                minQ.append(nums[r])
                maxQ.append(nums[r])
                r += 1
            else:
                if nums[l] == minQ[0]:
                    minQ.popleft()
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                l += 1
            result = max(result, r - l)
        return result