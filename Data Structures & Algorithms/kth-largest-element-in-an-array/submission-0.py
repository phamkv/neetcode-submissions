class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        heapq.heapify(result)
        for num in nums:
            heapq.heappush(result, num)
            if len(result) > k:
                heapq.heappop(result)
        return result[-(k)]