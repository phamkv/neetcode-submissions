class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        invert = [-val for val in stones]
        heapq.heapify(invert)
        while len(invert) > 1:
            biggest = heapq.heappop(invert)
            secondBiggest = heapq.heappop(invert)
            res = abs(-biggest - -secondBiggest)
            if res > 0:
                heapq.heappush(invert, -res)
        return 0 if len(invert) < 1 else -invert[0]