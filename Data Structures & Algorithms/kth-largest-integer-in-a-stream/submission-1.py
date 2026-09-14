class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minH = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minH) < self.k:
            heapq.heappush(self.minH, val)
        else:
            heapq.heappushpop(self.minH, val)
        return self.minH[0]
